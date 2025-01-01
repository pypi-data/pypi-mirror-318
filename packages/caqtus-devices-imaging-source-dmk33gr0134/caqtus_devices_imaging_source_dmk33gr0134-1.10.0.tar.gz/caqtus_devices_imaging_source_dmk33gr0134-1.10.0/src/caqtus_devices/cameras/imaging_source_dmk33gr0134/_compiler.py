from caqtus.device import DeviceName
from caqtus.device.camera import CameraCompiler
from caqtus.shot_compilation import SequenceContext

from .configuration import ImagingSourceCameraConfiguration


class ImagingSourceCameraCompiler(CameraCompiler):
    def __init__(self, device_name: DeviceName, sequence_context: SequenceContext):
        super().__init__(device_name, sequence_context)
        configuration = sequence_context.get_device_configuration(device_name)
        if not isinstance(configuration, ImagingSourceCameraConfiguration):
            raise TypeError(
                f"Expected {ImagingSourceCameraConfiguration} for device {device_name}, "
                f"got {type(configuration)}"
            )
        self.configuration = configuration
        self.device_name = device_name

    class InitParams(CameraCompiler.CameraInitializationParameters):
        camera_name: str
        format: str

    def compile_initialization_parameters(self) -> InitParams:
        return self.InitParams(
            **super().compile_initialization_parameters(),
            camera_name=self.configuration.camera_name,
            format=self.configuration.format,
        )
