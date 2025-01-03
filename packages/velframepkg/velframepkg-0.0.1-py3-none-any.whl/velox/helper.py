# Copyright(c) 2021 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import squish


def default_mouse_drag(tab_content, direction="default"):
    """Perform a mouse drag on an image. The default direction is used to draw a line or rectangle and dimension don't
    matter.

    Parameters
    ----------
    tab_content: Tab object reference
    direction: Direction in with the drag will be performed.
    """
    direction = direction.lower()
    assert direction in ["left", "right", "up", "down", "default"]
    middle_x = int(tab_content.width / 2)
    middle_y = int(tab_content.height / 2)
    delta = int(min(tab_content.width, tab_content.height) / 3)
    if direction == "left":
        start_x = middle_x + delta
        start_y = middle_y
        finish_x = 0 - delta
        finish_y = 0
    elif direction == "right":
        start_x = middle_x - delta
        start_y = middle_y
        finish_x = delta
        finish_y = 0
    elif direction == "up":
        start_x = middle_x
        start_y = middle_y + delta
        finish_x = 0
        finish_y = 0 - delta
    elif direction == "down":
        start_x = middle_x
        start_y = middle_y - delta
        finish_x = 0
        finish_y = delta
    else:
        start_x = middle_x - delta
        start_y = middle_y - delta
        finish_x = delta * 2
        finish_y = finish_x

    squish.mouseDrag(
        tab_content,
        start_x,
        start_y,
        finish_x,
        finish_y,
        squish.Qt.NoModifier,
        squish.MouseButton.LeftButton,
    )
