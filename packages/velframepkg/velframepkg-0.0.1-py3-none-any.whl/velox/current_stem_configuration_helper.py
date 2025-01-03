# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
from velox.labels.acquisition_toolbar import StemDetectorFamily


def get_current_stem_configuration() -> StemDetectorFamily:
    """Get from the simulator the current stem configuration."""
    from TemServer import Detector, instrument

    # Make sure we always have no rotation
    instrument.column.set_rotation(0)

    if instrument.stem_detector.is_present(Detector.DF4):
        return StemDetectorFamily.DF4
    elif instrument.stem_detector.is_present(Detector.DF_S):
        return StemDetectorFamily.DFS
    elif instrument.stem_detector.is_present(Detector.HAADF):
        return StemDetectorFamily.HAADF_ONLY
    else:
        return StemDetectorFamily.UNKNOWN
