# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import squish

from velox.application import Application
from velox.object_map.global_object_map import (
    a_detectorRotationOffsetPanel_offset_lineEdit,
    a_detectorRotationOffsetPanel_OK_button,
    a_stemRotationToolbar_editRotation_lineEdit,
)


class DetectorRotationHelper:
    """Provides some helper functions related to the detector rotation feature."""

    @staticmethod
    def set_detector_rotation_offset(offset):
        """Specifies the rotation offset of the detector.

        Parameters
        ----------
        offset: Rotation offset (Unit: degree)
        """

        application = Application()
        application.acquisition.menu.menu_dpc.detector_rotation_offset()

        # Fills the dialog box
        detector_rotation_offset_widget = squish.waitForObject(a_detectorRotationOffsetPanel_offset_lineEdit)

        if detector_rotation_offset_widget is not None:
            squish.type(detector_rotation_offset_widget, str(offset))

        squish.clickButton(squish.waitForObject(a_detectorRotationOffsetPanel_OK_button))

    @staticmethod
    def get_displayed_scan_rotation():
        """Retrieves the scan rotation (application side) (Unit: degree)"""

        scan_rotation_widget = squish.waitForObject(a_stemRotationToolbar_editRotation_lineEdit)
        displayed_rotation = float(str(scan_rotation_widget.text)[:-1])
        return displayed_rotation
