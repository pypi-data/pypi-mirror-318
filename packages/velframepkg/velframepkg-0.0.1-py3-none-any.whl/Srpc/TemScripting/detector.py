# Copyright(c) 2022 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
from dataclasses import dataclass
from enum import Enum


class Detector(Enum):
    HAADF = "HAADF"
    BF = "BF"
    DF4 = "DF4"
    DF2 = "DF2"
    DF4_A = "DF4-A"  # First segment of DF4 multi segment detector
    DF_I = "DF-I"  # Inner ring segment of DF-S detector
    DF_O = "DF-O"  # Outer ring segment of DF-S detector
    DF_S = "DF-S"
    BF_S = "BF-S"
    DF_2 = "DF-2"


class Camera(Enum):
    BM_Ceta = "BM-Ceta"
    BM_Dragonfly = "BM-Dragonfly"
    BM_Falcon = "BM-Falcon"
    BM_OneView = "BM-OneView"
    BM_Orius = "BM-Orius"
    BM_Standalone = "BM-Standalone"
    BM_UltraScan = "BM-UltraScan"
    BM_US1000XP = "BM-US1000XP"


class InstrumentMode(Enum):
    TEM = "TEM"
    STEM = "STEM"


class HolderType(Enum):
    NONE = "None"
    SINGLE_TILT = "SingleTilt"
    DOUBLE_TILT = "DoubleTilt"
    POLARA = "Polara"
    DUAL_AXIS = "DualAxis"
    ROTATION_AXIS = "RotationAxis"
    UNKNOWN = "UNKNOWN"


class Segment(Enum):
    Segment1 = 0
    Segment2 = 1
    Segment3 = 2
    Segment4 = 3
    Segment5 = 4
    Segment6 = 5


@dataclass
class Position:
    x: float
    y: float
    z: float
    alpha: float
    beta: float
