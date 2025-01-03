# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import squish
import test

from common.labels.widgets_states import WidgetChecked
from utils.labels.menu_access import MenuAccess, MenuIndex, SubMenuIndex


class Menu:
    def __init__(self, model):
        self.__model = model

    @staticmethod
    def __process_accelerate(values):
        for keys in values:
            squish.nativeType(keys)

    @staticmethod
    def __process_shortcut(values):
        squish.nativeType(values)

    @staticmethod
    def __process_click(values, expected_state: WidgetChecked):
        last_index = len(values) - 1
        for i in range(len(values)):
            squish.snooze(0.5)  # half a second delay due to the flakiness of the menu options in eds menu
            obj = squish.waitForObjectItem(
                values[i][MenuIndex.OBJECT_INDEX.value], values[i][MenuIndex.ITEM_INDEX.value]
            )
            if i != last_index:
                squish.mouseClick(obj)
            else:
                if bool(expected_state) != obj.checked:
                    squish.mouseClick(obj)
                else:
                    test.log(f"option is {expected_state.value} already")
            if i + 1 < len(values):
                squish.waitForObject(values[i + 1][MenuIndex.OBJECT_INDEX.value])

    def select_menu_item(self, action, access, expected_state: WidgetChecked = WidgetChecked.CHECKED):
        if action in self.__model and access in self.__model[action]:
            values = self.__model[action][access]
            if access == MenuAccess.CLICK:
                Menu.__process_click(values, expected_state)
            elif access == MenuAccess.ACCELERATE:
                Menu.__process_accelerate(values)
            elif access == MenuAccess.SHORTCUT:
                Menu.__process_shortcut(values)

    def deselect_menu_item(self, action, access, expected_state: WidgetChecked = WidgetChecked.UNCHECKED):
        if action in self.__model and access in self.__model[action]:
            values = self.__model[action][access]
            if access == MenuAccess.CLICK:
                Menu.__process_click(values, expected_state)
            elif access == MenuAccess.ACCELERATE:
                Menu.__process_accelerate(values)
            elif access == MenuAccess.SHORTCUT:
                Menu.__process_shortcut(values)

    def get_menu_item_selection(self, action) -> WidgetChecked:
        """Returns the selection status for a given action.

        Parameters
        ----------
        action: action from which retrieve the current selection state

        Returns
        -------
        item selection status of type WidgetChecked
        """
        if action in self.__model:
            value = self.__model[action][MenuAccess.CLICK]
            squish.mouseClick(
                squish.waitForObjectItem(
                    value[SubMenuIndex.MAIN_MENU_INDEX.value][MenuIndex.OBJECT_INDEX.value],
                    value[SubMenuIndex.MAIN_MENU_INDEX.value][MenuIndex.ITEM_INDEX.value],
                )
            )
            status = squish.waitForObjectItem(
                value[SubMenuIndex.SUB_MENU_INDEX.value][MenuIndex.OBJECT_INDEX.value],
                value[SubMenuIndex.SUB_MENU_INDEX.value][MenuIndex.ITEM_INDEX.value],
            ).checked
            # close menu
            squish.mouseClick(
                squish.waitForObject(value[SubMenuIndex.MAIN_MENU_INDEX.value][MenuIndex.OBJECT_INDEX.value])
            )
            return WidgetChecked.CHECKED if status else WidgetChecked.UNCHECKED
