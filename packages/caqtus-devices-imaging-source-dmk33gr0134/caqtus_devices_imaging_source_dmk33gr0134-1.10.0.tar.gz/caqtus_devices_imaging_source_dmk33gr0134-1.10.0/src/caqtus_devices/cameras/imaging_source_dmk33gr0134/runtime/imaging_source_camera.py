"""This module provide a class to use an Imaging Source camera."""

import contextlib
import ctypes
import logging
import os
from typing import Literal, ClassVar, Self

import attrs
import numpy

import caqtus.formatter as fmt
from caqtus.device.camera import Camera, CameraTimeoutError
from caqtus.types.recoverable_exceptions import (
    ConnectionFailedError,
    RecoverableException,
)
from caqtus.utils.context_managers import close_on_error
from . import tisgrabber as tis

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

tisgrabber_path = (
    os.path.expanduser("~")
    + r"\Documents\The Imaging Source Europe GmbH\TIS Grabber DLL\bin\x64\tisgrabber_x64.dll"
)

ic = ctypes.cdll.LoadLibrary(tisgrabber_path)
tis.declareFunctions(ic)

ic.IC_InitLibrary(0)

_MAP_FORMAT = {"Y16": 4, "Y800": 0}


@attrs.define(slots=False)
class ImagingSourceCameraDMK33GR0134(Camera):
    """Class to use an Imaging Source camera DMK33GR0134.

    Warning:
        This class only sets the camera exposure time, trigger and format.
        Other settings such as brightness, contrast, sharpness, gamma, and gain are
        not implemented and keep the value set before acquiring the camera.

    Attributes:
        camera_name: The name of the camera
        format: The format of the camera.
        Can be "Y16" or "Y800" respectively for 16-bit and 8-bit monochrome images.
    """

    sensor_width: ClassVar[int] = 1280
    sensor_height: ClassVar[int] = 960

    camera_name: str = attrs.field(
        validator=attrs.validators.instance_of(str), on_setattr=attrs.setters.frozen
    )
    format: Literal["Y16", "Y800"] = attrs.field(
        validator=attrs.validators.in_(["Y16", "Y800"]), on_setattr=attrs.setters.frozen
    )

    _grabber_handle = attrs.field(init=False)
    _close_stack: contextlib.ExitStack = attrs.field(
        init=False, factory=contextlib.ExitStack
    )

    @classmethod
    def get_device_names(cls) -> list[str]:
        """Return the names of the Imaging Source cameras connected to the computer."""

        return [
            tis.D(ic.IC_GetUniqueNamefromList(i))
            for i in range(cls.get_device_counts())
        ]

    @classmethod
    def get_device_counts(cls) -> int:
        """Return the number of Imaging Source cameras connected to the computer."""

        return ic.IC_GetDeviceCount()

    def __enter__(self) -> Self:
        with close_on_error(self._close_stack):
            self._initialize()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._close_stack.__exit__(exc_type, exc_val, exc_tb)

    def _initialize(self):
        self._grabber_handle = ic.IC_CreateGrabber()
        self._close_stack.callback(ic.IC_ReleaseGrabber, self._grabber_handle)

        ic.IC_OpenDevByUniqueName(self._grabber_handle, tis.T(self.camera_name))
        if not ic.IC_IsDevValid(self._grabber_handle):
            raise ConnectionFailedError(
                f"Could not find camera with "
                f"{fmt.device_param('camera name', self.camera_name)}"
            )

        self._set_format(self.format)
        self._set_trigger(self.external_trigger)

        self._start_live()
        self._close_stack.callback(self._stop_live)

    def _start_live(self) -> None:
        if not ic.IC_StartLive(self._grabber_handle, 0):
            error = FailedToStartLive("Failed to start live acquisition")
            error.add_note("Maybe check that the camera is not open by another program")
            raise error

    def _stop_live(self) -> None:
        if not ic.IC_StopLive(self._grabber_handle):
            raise RuntimeError("Failed to stop live")

    def update_parameters(self, timeout: float) -> None:
        self.timeout = timeout

    @contextlib.contextmanager
    def acquire(self, exposures: list[float]):
        yield self._read_images(exposures)

    def _read_images(self, exposures: list[float]):
        current_exposure = None
        for exposure in exposures:
            if exposure != current_exposure:
                self._set_exposure(exposure)
                current_exposure = exposure
            self._snap_picture()
            yield self._read_picture_from_camera()

    def _set_trigger(self, external_trigger: bool):
        if (
            ic.IC_EnableTrigger(self._grabber_handle, int(external_trigger))
            != tis.IC_SUCCESS
        ):
            raise RuntimeError(f"Failed to set trigger mode to {external_trigger}")

    def _set_format(self, format_: Literal["Y16", "Y800"]):
        if not ic.IC_SetFormat(self._grabber_handle, _MAP_FORMAT[format_]):
            raise RuntimeError("Failed to set format")

    def _set_exposure(self, exposure: float):
        ic.IC_SetPropertyAbsoluteValue(
            self._grabber_handle,
            tis.T("Exposure"),
            tis.T("Value"),
            ctypes.c_float(exposure),
        )

    def _snap_picture(self) -> None:
        timeout = int(self.timeout * 1e3)
        result = ic.IC_SnapImage(self._grabber_handle, timeout)
        if result != tis.IC_SUCCESS:
            raise CameraTimeoutError("Failed to acquire picture")

    def _read_picture_from_camera(self) -> numpy.ndarray:
        width = ctypes.c_long()
        height = ctypes.c_long()
        bits_per_pixel = ctypes.c_int()
        color_format = ctypes.c_int()

        ic.IC_GetImageDescription(
            self._grabber_handle, width, height, bits_per_pixel, color_format
        )

        buffer_size = width.value * height.value * bits_per_pixel.value

        image_ptr = ic.IC_GetImagePtr(self._grabber_handle)

        data = ctypes.cast(image_ptr, ctypes.POINTER(ctypes.c_ubyte * buffer_size))

        bytes_per_pixel = int(bits_per_pixel.value / 8.0)
        image = numpy.ndarray(
            buffer=data.contents,
            dtype=numpy.uint8,
            shape=(height.value, width.value, bytes_per_pixel),
        )
        formatted_image = _reformat_image(image, self.format).transpose()
        roi = (
            slice(self.roi.x, self.roi.x + self.roi.width),
            slice(self.roi.y, self.roi.y + self.roi.height),
        )
        return formatted_image[roi]


class FailedToStartLive(RecoverableException):
    """Raised when the camera failed to start live."""

    pass


def _reformat_image(image: numpy.ndarray, format_: str) -> numpy.ndarray:
    height, width, bytes_per_pixel = image.shape
    if format_ == "Y16":
        new_image = numpy.zeros((height, width), dtype=numpy.uint16)
        new_image[:, :] = image[:, :, 0] + image[:, :, 1] * 256
    elif format_ == "Y800":
        new_image = numpy.zeros((height, width), dtype=numpy.uint8)
        new_image[:, :] = image[:, :, 0]
    else:
        raise NotImplementedError(f"Format {format_} not implemented")
    return new_image

    # def save_state_to_file(self, file):
    #     if (
    #         ic.IC_SaveDeviceStateToFile(self._grabber_handle, T(str(file)))
    #         != IC_SUCCESS
    #     ):
    #         raise RuntimeError(f"Failed to save state to file {file}")

    # def load_state_from_file(self, file):
    #     if (
    #         error := ic.IC_LoadDeviceStateFromFile(self._grabber_handle, T(str(file)))
    #     ) != IC_SUCCESS:
    #         raise RuntimeError(f"Failed to load state from file {file}: {error}")

    # def reset_properties(self):
    #     if (error := ic.IC_ResetProperties(self._grabber_handle)) != IC_SUCCESS:
    #         pass  # not sure why, but the line above returns an error
    #         # raise RuntimeError(f"Failed to reset properties for {self.name}: {error}")

    # def _setup_properties(self):
    #     if not ic.IC_SetFormat(self._grabber_handle, _MAP_FORMAT[self.format]):
    #         raise RuntimeError("Failed to set format")
    #     if not ic.IC_SetPropertyValue(
    #         self._grabber_handle, T("Brightness"), T("Value"), self.brightness
    #     ):
    #         raise RuntimeError("Failed to set brightness")
    #     if not ic.IC_SetPropertyValue(
    #         self._grabber_handle, T("Contrast"), T("Value"), self.contrast
    #     ):
    #         raise RuntimeError("Failed to set contrast")
    #     if not ic.IC_SetPropertyValue(
    #         self._grabber_handle, T("Sharpness"), T("Value"), self.sharpness
    #     ):
    #         raise RuntimeError("Failed to set sharpness")
    #     if not ic.IC_SetPropertyAbsoluteValue(
    #         self._grabber_handle, T("Gamma"), T("Value"), ctypes.c_float(self.gamma)
    #     ):
    #         raise RuntimeError("Failed to set gamma")
    #     if not ic.IC_SetPropertySwitch(self._grabber_handle, T("Gain"), T("Auto"), 0):
    #         raise RuntimeError("Failed to set gain to manual")
    #     if not ic.IC_SetPropertyAbsoluteValue(
    #         self._grabber_handle, T("Gain"), T("Value"), ctypes.c_float(self.gain)
    #     ):
    #         raise RuntimeError("Failed to set gain")
    #     if not ic.IC_SetPropertySwitch(
    #         self._grabber_handle, T("Exposure"), T("Auto"), 0
    #     ):
    #         raise RuntimeError("Failed to set exposure to manual")
    #
    #     if not ic.IC_SetPropertySwitch(
    #         self._grabber_handle, T("Exposure"), T("Auto"), 0
    #     ):
    #         raise RuntimeError("Failed to set exposure to manual")
