# Copyright(c) 2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import squish
from screen import Screen


def refresh_taskbar_icons():
    """Refreshes the icons in the Windows taskbar by moving the mouse over the taskbar.

    This is necessary because when application with tray icons like OBS are killed, the icon remains in the system tray
    until it is manually refreshed by running the mouse over it.
    """
    relative_y_taskbar_position = 0.985
    relative_halfway_position = 0.5
    nr_of_mouse_passes = 2
    geom = Screen.byIndex(0).geometry
    y_middle_taskbar = int(geom.height * relative_y_taskbar_position)
    horizontal_range = range(geom.width, int(geom.width * relative_halfway_position), -1)

    for _ in range(nr_of_mouse_passes):
        for x in horizontal_range:
            squish.mouseMove(x, y_middle_taskbar)
