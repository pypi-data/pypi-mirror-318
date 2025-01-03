# Copyright(c) 2021 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import squish

from toplevelwindow import ToplevelWindow
from velox.object_map.acquisition.acquisition_object_map import acquisition_window
from velox.object_map.processing.processing_object_map import processing_window


def set_horizontal_layout():
    acq_win = squish.waitForObject(acquisition_window)
    pro_win = squish.waitForObject(processing_window)

    window = ToplevelWindow.byName(acquisition_window)
    window.maximize()

    width = acq_win.width
    height = acq_win.height

    squish.setWindowState(acq_win, squish.WindowState.Normal)
    acq_win.move(0, 0)
    acq_win.resize(width, height / 2)
    squish.setWindowState(pro_win, squish.WindowState.Normal)
    pro_win.move(0, height / 2)
    pro_win.resize(width, height / 2)

    window = ToplevelWindow.byName(acquisition_window)
    window.setForeground()
    window.setFocus()
