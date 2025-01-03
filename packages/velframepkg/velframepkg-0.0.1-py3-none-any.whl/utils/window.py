# Copyright(c) 2023-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

from typing import Tuple

from basic.components import Component
from toplevelwindow import ToplevelWindow


class Window(Component):
    def __init__(self, symbolic_name: dict, name: str):
        super().__init__(name, symbolic_name)
        self.window = ToplevelWindow.byName(symbolic_name)

    def maximize(self):
        self.window.maximize()
        self.window.setForeground()
        self.window.setFocus()

    def minimize(self):
        self.window.minimize()

    def focus(self):
        """Gives focus to this window."""
        self.minimize()
        self.maximize()

    def window_title(self) -> str:
        return str(self.window.windowTitle)

    def close(self):
        """Closes the given window.

        Simulates the action of closing the window using window close (X) button
        """
        self.window.close()

    def move_to(self, x_cord: int, y_cord: int):
        """Moves the Top level window to the given cordinates.

        Parameters
        ----------
        x_cord, y_cord: x and y coordinates to which the window is to be moved
        """
        self.window.setForeground()
        self.window.setFocus()
        self.window.moveTo(x_cord, y_cord)

    def resize_to(self, width: int, height: int):
        """Resizes the Top level window to the given dimensions.

        Parameters
        ----------
        width: new width of the window
        height: new height of the window
        """
        self.window.setForeground()
        self.window.setFocus()
        self.window.resizeTo(width, height)

    def restore(self):
        """Restores the given window."""
        self.window.restore()

    @property
    def position(self) -> Tuple[int, int]:
        """Get the window position on the screen, in the form of tuple".

        Parameters
         ----------
         window_name: window name for which dimensions are to be found

         Returns
         -------
         Tuple[int, int]
             x and y coordinates of the position of window on the screen
        """

        geometry = self.window.geometry
        return (geometry.x, geometry.y)

    @property
    def dimensions(self) -> Tuple[int, int]:
        """Get the window dimensions, in the form of tuple".

        Parameters
        ----------
        window_name: window name for which dimensions are to be found

        Returns
        -------
        Tuple[int, int]
            width and height of the given window
        """

        geometry = self.window.geometry
        return (geometry.width, geometry.height)
