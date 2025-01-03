# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import squish
import test

from common import CommonApplication
from velox.dialog.startup_dialog import StartupDialog
from velox.labels.velox_application import VeloxCommandLineOptions
from velox.labels.window_type import WindowType
from velox.window.acquisition_window import AcquisitionWindow
from velox.window.processing_window import ProcessingWindow


class Application(CommonApplication):
    def __init__(self, offline: bool, parameters: VeloxCommandLineOptions):
        application_name = "Velox"
        super().__init__(application_name, str(parameters))
        self._offline = offline

    def is_offline(self):
        return self._offline

    def start(self, *args, **kwargs) -> None:
        super().start(*args, **kwargs)

        attempt = 1
        while StartupDialog.opengl_shading_language_error_occurred():
            if attempt >= 10:
                raise RuntimeError("Unable to start Velox because of OpenGL shading language version error.")

            test.warning("OpenGL shading language error occurred.")
            StartupDialog.close()
            squish.snooze(60)
            super().start(*args, **kwargs)

            attempt += 1

        if self.is_offline():
            self.processing = ProcessingWindow()
        else:
            self.acquisition = AcquisitionWindow()
            self.processing = ProcessingWindow()

    def switch_window(self, window_name: WindowType):
        if self.is_offline():
            self.processing.maximize()
            return
        if window_name == WindowType.ACQUISITION:
            self.processing.minimize()
            self.acquisition.maximize()
        elif window_name == WindowType.PROCESSING:
            self.acquisition.minimize()
            self.processing.maximize()
        else:
            test.fail(f"Unexpected window: {window_name.value}")
