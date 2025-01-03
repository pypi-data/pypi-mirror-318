# Copyright(c) 2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import os
import re
import time

from pywinauto.application import Application


class ExternalAccessUI:
    def __init__(self) -> None:
        """Creates an instance of this class and sets the path for the app in srpc directory."""
        srpc_app_directory = os.path.dirname(os.path.realpath(__file__))
        self.__app_path = os.path.join(srpc_app_directory, "TestEdxTomography.exe")
        self.event_log = []

    def start(self):
        """Starts the external access app."""
        self.__app = Application(backend="uia").start(self.__app_path)
        self.__window = self.__app.top_window()
        self.__window.wait("ready", 300, 1)
        self.__window.set_focus()

    def connect(self):
        """Clicks the connect button in the external access app."""
        self.__window.Connect.click_input()

    def disconnect(self):
        """Clicks the disconnect button in the external access app."""
        self.__window.Disconnect.click_input()

    def get_acquisition_time(self) -> float:
        """Gets the acquisition time computed by the external access app.

        Returns
        -------
        The acquisition time, in seconds, as a float.
        """
        self.__window.Button5.click_input()
        return float(self.__window.Edit4.get_value())

    def clear_log(self):
        """Clears the log of the external access app."""
        self.__window.Clear.click_input()

    def set_acquisition_modes(self, modes: list):
        """Sets the acquisition modes to use in the external access app.

        Parameters
        ----------
        modes: a list of acquisition modes to be set
        """
        list_box = self.__window.ListBox
        for list_item in list_box.get_items():
            mode = list_item.texts()[0]
            if mode in modes:
                list_item.click_input()

    def start_acquisition(self):
        """Clicks the start mapping button in the external access app."""
        self.__window["Start Mapping"].click_input()

    def __update_event_log(self):
        """Helper function to update the event log."""
        new_entries = [line for line in self.__window.Edit2.get_value().split("\r") if line]
        self.clear_log()

        self.event_log = self.event_log + new_entries

    def wait_until_acquisition_finished(self) -> float:
        """Waits until the finished acquisition message shows in the logs of the external access app.

        Returns
        -------
        The time, in seconds, the acquisition took, as a float.
        """
        finished_pattern = r"Finished acquisition, it took: (\d*\.?\d*)"
        for i in range(10):
            self.__update_event_log()
            match = re.search(finished_pattern, self.event_log[-1])
            if match:
                return float(match.group(1))
            time.sleep(2)
        return -1

    def close(self):
        """Closes the external access app."""
        self.__window.close()

    def get_experiment_directory(self) -> str:
        """Gets the experiment directory from the external access app."""
        return self.__window.Edit5.get_value()

    def set_output_mode(self, output_mode: str):
        """Sets the output mode of external access app.

        Parameters
        ----------
        output_mode: the output mode to set
        """
        if output_mode != self.__window.OutputComboBox.selected_text():
            self.__window.OutputComboBox.select(output_mode)
