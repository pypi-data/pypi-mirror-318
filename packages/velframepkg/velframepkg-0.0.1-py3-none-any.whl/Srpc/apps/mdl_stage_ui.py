# Copyright(c) 2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
from pywinauto.application import Application

MDL_STAGE_UI_PATH = r"C:\Tecnai\Exe\Service\MdlStageUI.exe"


class MdlStageUI:
    """This class uses pywinauto to control the MdlStageUI application."""

    def start(self):
        """Opens the app with pywinauto."""
        self.__app = Application(backend="uia").start(MDL_STAGE_UI_PATH)
        self.__window = self.__app.top_window()
        self.__window.child_window(title="Holder detected", auto_id="holderDetected", control_type="CheckBox").wait(
            "ready", 300, 1
        )
        self.__holder_detected_checkbox = self.__window.child_window(
            title="Holder detected", auto_id="holderDetected", control_type="CheckBox"
        ).wrapper_object()

    def click_holder_detected_checkbox(self):
        """Clicks the holder detected checkbox in the application."""
        self.__holder_detected_checkbox.click()

    def is_holder_detected_checked(self) -> bool:
        """Returns whether the holder detected checkbox is checked.

        Returns
        -------
        True if holder detected checkbox is checked, False otherwise
        """
        return self.__holder_detected_checkbox.get_toggle_state() == 1

    def close(self):
        """Closes the application."""
        self.__window.close()
