"""Communicate with the basler camera."""

import numpy as np
from pypylon import genicam, pylon

from .units import u


class BaslerCam:
    """Run a generic Basler camera, copied heavily from grab.py code online."""

    def __init__(self, px_size_um: float = 3.45, debug: bool = True) -> None:
        """Initialize the camera.

        :param px_size_um: Pixel size in um
        """
        # pixel size
        self.px_size = px_size_um * u.um

        self.debug = debug
        self.cam = pylon.InstantCamera(
            pylon.TlFactory.GetInstance().CreateFirstDevice()
        )
        self.cam.Open()

        self.exposure_time = 1000  # expsoure time in us

        self.cam.ExposureAuto.SetValue("Off")
        self.cam.ExposureTime.SetValue(self.exposure_time)

        if self.debug:
            print("Using device ", self.cam.GetDeviceInfo().GetModelName())

    def capture_image(self) -> np.array:
        """Grab an image."""
        # self.cam.Exposur
        result = self.cam.GrabOne(1000)
        return result.Array

    def find_exposure_time(self, min_peak: int = 200, max_peak: int = 255) -> None:
        """find exposure time automatically."""
        pass


if __name__ == "__main__":
    app = BaslerCam()
