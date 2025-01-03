# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import re

from basic.components import Window
from velox.object_map.processing.processing_object_map import processing_window


class Experiment:
    def __init__(self):
        self.__window = Window("Processing window", processing_window)
        self.__modified = False
        self.__loaded = False
        self.__experiment_name = ""

    def update(self):
        """Gets the experiment name from the window title and sets the modified and loaded attributes."""
        result = re.search(r".+\.emd|.+\.mrc|.+\.msa", self.__window.title)

        if result:
            experiment_name = result.group()

            self.__loaded = True

            if experiment_name.startswith("*"):
                self.__modified = True
                self.__experiment_name = experiment_name[1:]
            else:
                self.__modified = False
                self.__experiment_name = experiment_name
        else:
            self.__modified = False
            self.__loaded = False
            self.__experiment_name = ""

    @property
    def name(self):
        self.update()
        return self.__experiment_name

    @property
    def modified(self):
        self.update()
        return self.__modified

    @property
    def loaded(self):
        self.update()
        return self.__loaded
