# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import squish
import test

from apollo.dialog.startup_dialog import StartupDialog
from apollo.labels.mico_application import MiCoCommandLineOptions
from apollo.window.apollo_window import ApolloWindow
from common import CommonApplication


class Application(CommonApplication):
    def __init__(self, parameters: MiCoCommandLineOptions):
        application_name = "MiCo"
        super().__init__(application_name, str(parameters))

    def start(self, *args, **kwargs) -> None:
        super().start(*args, **kwargs)

        attempt = 1
        while StartupDialog.opengl_shading_language_error_occurred():
            if attempt >= 10:
                raise RuntimeError("Unable to start MiCo because of OpenGL shading language version error.")

            test.warning("OpenGL shading language error occurred.")
            StartupDialog.close()
            squish.snooze(60)
            super().start(*args, **kwargs)

            attempt += 1

        self.acquisition = ApolloWindow()
        self.acquisition.maximize()
