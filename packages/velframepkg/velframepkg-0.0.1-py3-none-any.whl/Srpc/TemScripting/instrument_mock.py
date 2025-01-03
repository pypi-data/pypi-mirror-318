# Copyright(c) 2022 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
from unittest.mock import MagicMock

from .detector import Camera, Detector, HolderType, InstrumentMode, Position, Segment

__all__ = ["Camera", "Detector", "HolderType", "InstrumentMode", "Position", "Segment"]

instrument = MagicMock()
