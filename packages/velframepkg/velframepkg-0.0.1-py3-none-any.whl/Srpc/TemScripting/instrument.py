# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

"""
ToDo: create unit tests and run on vm
ToDo: Add server-unit tests
ToDo: Reminder -> Align changes in file with the stub/interface file on this location: ./Squish/framework/TemServer.pyi

IInstrument4Connection  =>  IInstrument =>  Column (IomOpticsLib.IColumn2_4)    => IStage (IomStageLib.IStage)
                                                                                => ISource (IomGunLib.ISource)
                                                                                => IOptics (IomOpticsLib.IOptics3)
                                            Vacuum (IomVacuumLib.IVacuum2)
                                            Scan (IomAcquisitionScanLib.IScan)
                                            Detectors (IomCoreLib.IDetectors4)
                                            CommercialInfo (IomCommercialInfoLib.IConfiguration2)


"""

import ctypes
import math
import sys
from typing import Tuple, Union

# need to set this before actually importing comtypes to enforce MTA
sys.coinit_flags = 0  # pythoncom.COINIT_MULTITHREADED = 0

from comtypes import client  # noqa: E402

from .detector import Camera, Detector, HolderType, InstrumentMode, Position, Segment  # noqa: E402


class Instrument4Connection:
    IomCoreLib = client.GetModule("IomCore.dll")

    def __init__(self):
        self.connection = client.CreateObject(
            "Tem.Instrument4Connection", interface=Instrument4Connection.IomCoreLib.IInstrument4Connection
        )
        self.connection.Connect()
        self.instrument = self.connection.Instrument

    def disconnect(self):
        try:
            self.connection.Disconnect()
            del self.connection
            self.instrument = None
        except Exception as ex:
            print(
                "Unable to disconnect from connection.\n"
                f"An exception of type {type(ex).__name__} occurred.\n"
                f"Arguments:\n{ex.args}"
            )


class FeiComTypes:
    """This is a python com types FeiComTypes factory wrapper class."""

    FeiComTypesLib = client.GetModule("FeiComTypes.dll")

    @classmethod
    def coordinate_float(cls, x: float, y: float) -> FeiComTypesLib.ICoordinateFloat:
        coordinate = client.CreateObject(
            "Fei.Common.CoordinateFloat", interface=FeiComTypes.FeiComTypesLib.ICoordinateFloat
        )
        coordinate.x = ctypes.c_double(x)
        coordinate.y = ctypes.c_double(y)
        return coordinate

    @classmethod
    def size_2d_float(cls, width: float, height: float) -> FeiComTypesLib.ISize2DFloat:
        size = client.CreateObject("Fei.Common.Size2DFloat", interface=FeiComTypes.FeiComTypesLib.ISize2DFloat)
        size.x = width
        size.y = height
        return size


class PatternRenderer:
    """This is a python com types PatternRenderer factory wrapper class."""

    PatternRendererLib = client.GetModule("PatternRenderer.dll")
    Factory = client.CreateObject("PatternRenderer.PatternFactory", interface=PatternRendererLib.IPatternFactory)

    @classmethod
    def pattern_spot(cls, x: float, y: float, dwell_time: float) -> PatternRendererLib.IPatternSpot:
        assert 0 <= x <= 1, "Pattern value x must be between 0 and 1"
        assert 0 <= y <= 1, "Pattern value y must be between 0 and 1"
        return PatternRenderer.Factory.CreateSpot(FeiComTypes.coordinate_float(x, y), ctypes.c_double(dwell_time))

    @classmethod
    def spot_to_position(cls, pattern_spot: PatternRendererLib.IPattern) -> (float, float):
        new_spot = pattern_spot.QueryInterface(PatternRenderer.PatternRendererLib.IPatternSpot)
        return new_spot.Position.x, new_spot.Position.y


class IomAcquisition:
    IomAcquisitionLib = client.GetModule("IomAcquisition.dll")


class IomAcquisitionConnection:
    IomAcquisitionConnectionLib = client.GetModule("IomAcquisitionConnection.dll")


class IomVacuum:
    IomVacuumLib = client.GetModule("IomVacuum.dll")


class IomStage:
    IomStageLib = client.GetModule("IomStage.dll")


class IomAcquisitionCore:
    IomAcquisitionCoreLib = client.GetModule("IomAcquisitionCore.dll")


class IomAcquisitionStem:
    IomAcquisitionStemLib = client.GetModule("IomAcquisitionStem.dll")


class IomAcquisitionCamera:
    IomAcquisitionCameraLib = client.GetModule("IomAcquisitionCamera.dll")


class IomAcquisitionScan:
    IomAcquisitionScanLib = client.GetModule("IomAcquisitionScan.dll")


class IomFluScreen:
    IomFluScreenLib = client.GetModule("IomFluscreen.dll")


class IomOptics:
    IomOpticsLib = client.GetModule("IomOptics.dll")

    @classmethod
    def get_supported_column_interface(cls):
        if hasattr(IomOptics.IomOpticsLib, "IColumn2_5"):
            return IomOptics.IomOpticsLib.IColumn2_5
        elif hasattr(IomOptics.IomOpticsLib, "IColumn2_4"):
            return IomOptics.IomOpticsLib.IColumn2_4
        elif hasattr(IomOptics.IomOpticsLib, "IColumn2_3"):
            return IomOptics.IomOpticsLib.IColumn2_3
        elif hasattr(IomOptics.IomOpticsLib, "IColumn2_1"):
            return IomOptics.IomOpticsLib.IColumn2_1
        else:
            raise AssertionError(
                "TEM server is deprecated."
                " Please install a TEM server supporting one of these interfaces:"
                " IColumn2_5, IColumn2_4, IColumn2_3, IColumn2_1"
            )

    @classmethod
    def get_supported_column_mode_interface(cls):
        if hasattr(IomOptics.IomOpticsLib, "IColumn2_5"):
            if hasattr(IomOptics.IomOpticsLib, "IColumnMode2"):
                return IomOptics.IomOpticsLib.IColumn2_5
            else:
                return IomOptics.IomOpticsLib.IColumnMode

        elif hasattr(IomOptics.IomOpticsLib, "IColumn2_4"):
            return IomOptics.IomOpticsLib.IColumn2_4
        elif hasattr(IomOptics.IomOpticsLib, "IColumn2_3"):
            return IomOptics.IomOpticsLib.IColumn2_3
        elif hasattr(IomOptics.IomOpticsLib, "IColumn2_1"):
            return IomOptics.IomOpticsLib.IColumn2_1
        else:
            raise AssertionError(
                "TEM server is deprecated."
                " Please install a TEM server supporting one of these interfaces:"
                " IColumn2_5, IColumn2_4, IColumn2_3, IColumn2_1"
            )

    @classmethod
    def get_supported_optics_interface(cls):
        if hasattr(IomOptics.IomOpticsLib, "IOptics3"):
            return IomOptics.IomOpticsLib.IOptics3
        elif hasattr(IomOptics.IomOpticsLib, "IOptics2"):
            return IomOptics.IomOpticsLib.IOptics2
        else:
            raise AssertionError(
                "TEM server is deprecated."
                " Please install a TEM server supporting one of these interfaces:"
                " IOptics3, IOptics2"
            )


class IomGun:
    IomGunLib = client.GetModule("IomGun.dll")


class IomCommercialInfo:
    IomCommercialInfoLib = client.GetModule("IomComercialInfo.dll")

    @classmethod
    def get_supported_interface(cls):
        if hasattr(IomCommercialInfo.IomCommercialInfoLib, "IConfiguration2"):
            return IomCommercialInfo.IomCommercialInfoLib.IConfiguration2
        elif hasattr(IomCommercialInfo.IomCommercialInfoLib, "IConfiguration"):
            return IomCommercialInfo.IomCommercialInfoLib.IConfiguration
        else:
            raise AssertionError(
                "TEM server is deprecated."
                " Please install a TEM server supporting one of these interfaces:"
                " IConfiguration2, IConfiguration"
            )


def to_rad(degrees: float) -> float:
    return degrees / (180 / math.pi)


def to_degrees(rad: float) -> float:
    return rad * (180 / math.pi)


def to_micro(meters: float) -> float:
    """
    1.0 meter is 1000000.0 micrometer
    """
    return meters * 1000000


def to_meter(micro: float) -> float:
    """1000000.0 micrometer is 1.0 meter."""
    return micro / 1000000


class Column:
    def __init__(self, interface):
        self.interface = interface.Column.QueryInterface(IomOptics.get_supported_column_interface())
        if hasattr(IomOptics.IomOpticsLib, "IColumn2_5") and hasattr(IomOptics.IomOpticsLib, "IColumnMode2"):
            self.mode_interface = interface.Column.QueryInterface(IomOptics.IomOpticsLib.IColumn2_5)
        else:
            self.mode_interface = interface.Column.QueryInterface(IomOptics.get_supported_column_mode_interface())

    # Column interface
    def is_beam_blanked(self) -> bool:
        """Check if the beam is blanked.

        Returns
        -------
        bool
            True is the beam is blanked
        """
        return self.interface.GetBeamBlanked()

    def blank_beam(self):
        """Blanks the beam."""
        self.interface.BlankBeam()

    def un_blank_beam(self):
        """Un Blanks the beam."""
        self.interface.UnBlankBeam()

    def get_rotation(self) -> float:
        """Get the current rotation setting.

        Returns
        -------
        float
            Current rotation in degrees
        """
        return to_degrees(self.interface.GetScanRotation())

    def set_rotation(self, rotation: float):
        """Sets the detector rotation.

        Parameters
        ----------
        rotation : float
            Rotation to set in degrees
        """
        assert -360 <= rotation <= 360, "Rotation must be between -360 and 360 degrees"
        self.interface.SetScanRotation(to_rad(rotation))

    def get_instrument_mode(self) -> Union[InstrumentMode, None]:
        """Get the current instrument mode (TEM/STEM)

        Returns
        -------
        InstrumentMode
            The current instrument mode as an enum
        """
        if hasattr(IomOptics.IomOpticsLib, "IColumn2_5") and hasattr(IomOptics.IomOpticsLib, "IColumnMode2"):
            mode = self.mode_interface.GetMode().QueryInterface(IomOptics.IomOpticsLib.IColumnMode2)
        else:
            mode = self.mode_interface.GetMode()

        if (
            mode.ColumnOperatingMode == IomOptics.IomOpticsLib.enColumnOperatingMode_Stem
            and mode.ProjectorMode == IomOptics.IomOpticsLib.enProjectorMode_Diffraction
            and mode.ProbeMode == IomOptics.IomOpticsLib.enProbeMode_Nano
            and mode.ObjectiveMode == IomOptics.IomOpticsLib.enObjectiveMode_HM
            and mode.DarkFieldMode == IomOptics.IomOpticsLib.enDarkFieldMode_Off
        ):
            return InstrumentMode.STEM
        elif (
            mode.ColumnOperatingMode == IomOptics.IomOpticsLib.enColumnOperatingMode_Tem
            and mode.ProjectorMode == IomOptics.IomOpticsLib.enProjectorMode_Imaging
            and mode.ProbeMode == IomOptics.IomOpticsLib.enProbeMode_Micro
            and mode.ObjectiveMode == IomOptics.IomOpticsLib.enObjectiveMode_HM
        ):
            return InstrumentMode.TEM
        return None

    def set_instrument_mode(self, mode: InstrumentMode):
        """Set the instrument to given mode (TEM/STEM). Besides setting the correct mode it will also set a number of
        optical settings that align with the given TEM/STEM mode.

        Parameters
        ----------
        mode : InstrumentMode
            Instrument mode to set the instrument to as an enum
        """
        assert type(mode) == InstrumentMode, "mode parameter must be of type InstrumentMode"
        if self.get_instrument_mode() == mode:
            return

        if hasattr(IomOptics.IomOpticsLib, "IColumn2_5") and hasattr(IomOptics.IomOpticsLib, "IColumnMode2"):
            new_mode = self.mode_interface.GetMode().QueryInterface(IomOptics.IomOpticsLib.IColumnMode2)
        else:
            new_mode = self.interface.GetMode()

        if mode == InstrumentMode.STEM:
            new_mode.ColumnOperatingMode = IomOptics.IomOpticsLib.enColumnOperatingMode_Stem
            new_mode.ProjectorMode = IomOptics.IomOpticsLib.enProjectorMode_Diffraction
            new_mode.ProbeMode = IomOptics.IomOpticsLib.enProbeMode_Nano
            new_mode.ObjectiveMode = IomOptics.IomOpticsLib.enObjectiveMode_HM
            new_mode.DarkFieldMode = IomOptics.IomOpticsLib.enDarkFieldMode_Off
        elif mode == InstrumentMode.TEM:
            new_mode.ColumnOperatingMode = IomOptics.IomOpticsLib.enColumnOperatingMode_Tem
            new_mode.ProjectorMode = IomOptics.IomOpticsLib.enProjectorMode_Imaging
            new_mode.ProbeMode = IomOptics.IomOpticsLib.enProbeMode_Micro
            new_mode.ObjectiveMode = IomOptics.IomOpticsLib.enObjectiveMode_HM
        else:
            raise "Unknown"
        self.interface.SetMode(new_mode)

    class Stage:
        def __init__(self, interface):
            self.interface = interface.Stage.QueryInterface(IomStage.IomStageLib.IStage)

        def is_enabled(self) -> bool:
            """Checks if state is enabled.

            Returns
            -------
            bool
                Returns True if the stage is enabled
            """
            return self.interface.State == IomStage.IomStageLib.enStageState_Ready

        def get_position(self) -> Position:
            """Get the current stage position.

            Returns
            -------
            Position
                Stage position in microns on the axes (x,y,z) and degrees on rotations (a,b)
            """
            return Column.Stage._get_position(self.interface.Position)

        def set_position(self, x: float, y: float, z: float, alpha: float, beta: float):
            """Moves the stage to the given position.

            Parameters
            ----------
            x : float
                x-axis location in microns
            y : float
                y-axis location in microns
            z : float
                z-axis location in microns
            alpha : float
                alpha tilt in degrees
            beta : float
                beta tilt in degrees
            """
            position = self.interface.Position
            position.x = to_meter(x)
            position.y = to_meter(y)
            position.z = to_meter(z)
            position.a = to_rad(alpha)
            position.b = to_rad(beta)
            move_all_axis_mask = 31  # always move on all axis
            self.interface.Move(position, move_all_axis_mask)

        @classmethod
        def _get_position(cls, iom_position: IomStage.IomStageLib.IStage.Position) -> Position:
            return Position(
                to_micro(iom_position.x),
                to_micro(iom_position.y),
                to_micro(iom_position.z),
                to_degrees(iom_position.a),
                to_degrees(iom_position.b),
            )

    class BeamStopper:
        def __init__(self, interface):
            self.column_interface = interface.Column.QueryInterface(IomOptics.get_supported_column_interface())
            self.interface = self.column_interface.BeamStopper.QueryInterface(IomOptics.IomOpticsLib.IBeamStopper)

        def get_beamstop_state(self) -> int:
            """Gets BeamStop state from temserver.

                BeamStopperState_Unknown = 0,
                BeamStopperState_Out = 1,
                BeamStopperState_In = 2,
                BeamStopperState_HalfIn = 3,
                BeamStopperState_Busy = 4

            Returns
            -------
            BeamStop state as int
            """

            return self.interface.State

        def retract_beamstop(self):
            """Retracts BeamStop.

            Its state will be BeamStopperState_Out = 1
            """
            self.interface.Retract()

    class Holder:

        _holders = {
            IomStage.IomStageLib.enHolderType_Unknown: HolderType.NONE,
            IomStage.IomStageLib.enHolderType_SingleTilt: HolderType.SINGLE_TILT,
            IomStage.IomStageLib.enHolderType_DoubleTilt: HolderType.DOUBLE_TILT,
            IomStage.IomStageLib.enHolderType_Polara: HolderType.POLARA,
            IomStage.IomStageLib.enHolderType_DualAxis: HolderType.DUAL_AXIS,
            IomStage.IomStageLib.enHolderType_RotationAxis: HolderType.ROTATION_AXIS,
        }

        def __init__(self, interface):
            self.interface = interface.Stage.QueryInterface(IomStage.IomStageLib.IStage)

        def get_type(self) -> HolderType:
            """Returns the current holder type.

            Returns
            -------
            HolderType
                Holder type as a an enum
            """
            holder_type = self.interface.HolderType
            if holder_type in self._holders:
                return self._holders[holder_type]
            return HolderType.UNKNOWN

    class Source:
        def __init__(self, interface):
            self.interface = interface.Source.QueryInterface(IomGun.IomGunLib.ISource)

        def get_high_voltage(self) -> float:
            """Get the currently set high voltage.

            Returns
            -------
            float
                High voltage value in Volts
            """
            return self.interface.HighVoltage

        def set_high_voltage(self, voltage: float):
            """Set the high voltage setting.

            Parameters
            ----------
            voltage : float
                Value to set the high voltage to in volts
            """
            self.interface.SetHighVoltageAsync(voltage)

    class Optics:
        def __init__(self, interface):
            self.column_interface = interface.Column.QueryInterface(IomOptics.get_supported_column_interface())
            self.interface = interface.Optics.QueryInterface(IomOptics.get_supported_optics_interface())

        def get_tem_magnification(self) -> float:
            """Get the current TEM magnification value as shown to the user.

            Returns
            -------
            float
                Magnification set for TEM
            """
            return self.interface.GetMagnification().DisplayValue

        def set_tem_magnification_index(self, magnification_index: int):
            """Set the magnification index for TEM. Selects the given index from the list of magnifications available
            for the current mode.

            Parameters
            ----------
            magnification_index : int
                Index to select from list of available magnifications
            """
            magnifications = self.interface.GetMagnifications(self.column_interface.GetMode())
            assert magnification_index in range(len(magnifications)), "Magnification index outside magnification range"
            self.interface.SetMagnification(magnifications[magnification_index])

        def set_stem_magnification(self, magnification: int):
            """Set the stem magnification value.

            Parameters
            ----------
            magnification : int
                Magnification to set the stem mode to
            """
            set_magnification = self.interface.GetFullScanFieldOfView()
            set_magnification.x = 0.1 / magnification
            set_magnification.y = 0.1 / magnification
            self.interface.SetFullScanFieldOfView(set_magnification)


class FluScreen:
    def __init__(self, interface):
        self.interface = interface.QueryInterface(Instrument4Connection.IomCoreLib.IFluScreens)
        self.fluscreen1 = self.interface.FluScreen1.QueryInterface(IomFluScreen.IomFluScreenLib.IFluScreen)

    def insert(self):
        """Insert the Fluscreen."""
        self.fluscreen1.insert()

    def retract(self):
        """Retract the Fluscreen."""
        self.fluscreen1.retract()

    def is_inserted(self) -> bool:
        """Check if the Fluscreen is inserted.

        Returns
        -------
        bool
            True is camera is inserted
        """
        insertion_state = self.fluscreen1.GetInsertionState()
        return insertion_state == IomFluScreen.IomFluScreenLib.enFluScreenInsertionState_Inserted

    def is_retracted(self) -> bool:
        """Check if the Fluscreen is retracted.

        Returns
        -------
        bool
            True if the Fluscreen is retracted
        """
        insertion_state = self.fluscreen1.GetInsertionState()
        return insertion_state == IomFluScreen.IomFluScreenLib.enFluScreenInsertionState_Retracted


class Vacuum:
    def __init__(self, interface):
        self.interface = interface.QueryInterface(IomVacuum.IomVacuumLib.IVacuum2)

    def close_valves(self):
        """Close the column valves."""
        self.interface.CloseColumnValves()

    def open_valves(self):
        """Open the column valves."""
        self.interface.OpenColumnValves()

    def valves_are_open(self) -> bool:
        """Check if the column valves are open.

        Returns
        -------
        bool
            True if the valves are open
        """
        return self.interface.ColumnValvesState == IomVacuum.IomVacuumLib.enColumnValvesState_Opened

    def valves_are_not_allowed(self) -> bool:
        """Check if the column valves state is not allowed.

        Returns
        -------
        bool
            True if the valves state is not allowed
        """
        return self.interface.ColumnValvesState == IomVacuum.IomVacuumLib.enColumnValvesState_NotAllowed

    def is_ready(self) -> bool:
        """Checks if the Column vacuum state is ready.

        Returns
        -------
        bool
            True if there is vacuum in the column
        """
        return self.interface.State == IomVacuum.IomVacuumLib.enVacuumState_Ready

    def evacuate_all(self):
        """Evacuates the column thereby creating vacuum in the column."""
        if not self.is_ready():
            self.interface.Evacuate()


class Detectors:
    def __init__(self, interface):
        self.interface = interface

    class Camera:
        def __init__(self, interface):
            self.interface = interface.QueryInterface(Instrument4Connection.IomCoreLib.IDetectors4)

        def insert(self, camera: Camera):
            """Insert the camera.

            Parameters
            ----------
            camera : Camera
                Name of the camera as an enum
            """
            assert type(camera) == Camera, "camera parameter must be of type Camera"
            self._get_camera(camera).Insert()

        def retract(self, camera: Camera):
            """Retract the camera.

            Parameters
            ----------
            camera : Camera
                Name of the camera as an enum
            """
            assert type(camera) == Camera, "camera parameter must be of type Camera"
            self._get_camera(camera).Retract()

        def is_retracted(self, camera: Camera) -> bool:
            """Check if a camera is retracted.

            Parameters
            ----------
            camera : Camera
                Name of the camera as an enum

            Returns
            -------
            bool
                True is camera is retracted
            """
            assert type(camera) == Camera, "camera parameter must be of type Camera"
            insertion_state = self._get_camera(camera).GetInsertionState()
            return insertion_state == IomAcquisitionCore.IomAcquisitionCoreLib.DetectorInsertionState_Retracted

        def is_inserted(self, camera: Camera) -> bool:
            """Check if a camera is inserted.

            Parameters
            ----------
            camera : Camera
                Name of the camera as an enum

            Returns
            -------
            bool
                True is camera is inserted
            """
            assert type(camera) == Camera, "camera parameter must be of type Camera"
            insertion_state = self._get_camera(camera).GetInsertionState()
            return insertion_state == IomAcquisitionCore.IomAcquisitionCoreLib.DetectorInsertionState_Inserted

        def _get_camera(self, camera: Camera) -> Union[IomAcquisitionCore.IomAcquisitionCoreLib.IDetector2, None]:
            assert type(camera) == Camera, "camera parameter must be of type Camera"
            for camera_interface in self.interface.Cameras2:
                camera_obj = camera_interface.QueryInterface(IomAcquisitionCore.IomAcquisitionCoreLib.IDetector2)
                if camera_obj.Name != camera.value:
                    continue
                return camera_obj
            return None

    class StemDetector:

        has_multi_segment = [Detector.DF4]

        def __init__(self, interface):
            self.interface = interface.QueryInterface(Instrument4Connection.IomCoreLib.IDetectors4)

        def get_gain(self, detector: Detector) -> float:
            """Get the gain for a given detector.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum

            Returns
            -------
            float
                Gain as a percentage
            """
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            detector = self._get_detector(detector)
            return self._convert_to_percentage(detector.GetGainRange(), detector.GetGain())

        def get_offset(self, detector: Detector) -> float:
            """Get the offset for a given detector.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum

            Returns
            -------
            float
                Offset as a percentage
            """
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            detector = self._get_detector(detector)
            return self._convert_to_percentage(detector.GetOffsetRange(), detector.GetOffset())

        def get_segment_gain(self, detector: Detector, segment: Segment) -> float:
            """Get the gain for a segment of detector DF4.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum
            segment : Segment
                Segment to get the gain from as an enum

            Returns
            -------
            float
                Gain as a percentage
            """
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            assert type(segment) == Segment, "segment parameter must be of type Segment"
            detector = self._get_detector(detector)
            return self._convert_to_percentage(detector.GetGainRange(), detector.Segments[segment.value].GetGain())

        def get_segment_offset(self, detector: Detector, segment: Segment) -> float:
            """Get the offset for a segment of detector DF4.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum
            segment : Segment
                Segment to get the offset from as an enum

            Returns
            -------
            float
                Offset as a percentage
            """
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            assert type(segment) == Segment, "segment parameter must be of type Segment"
            detector = self._get_detector(detector)
            return self._convert_to_percentage(detector.GetOffsetRange(), detector.Segments[segment.value].GetOffset())

        def set_gain(self, detector: Detector, gain: float):
            """Set the gain for a given detector.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum
            gain : float
                Gain as a percentage
            """
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            assert 0 <= gain <= 100, "Gain must be between 0 and 100%"
            detector_obj = self._get_detector(detector)
            detector_obj.SetGain(self._convert_from_percentage(detector_obj.GetGainRange(), gain))

        def set_offset(self, detector: Detector, offset: float):
            """Set the offset for a given detector.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum
            offset : float
                Offset as a percentage
            """
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            assert 0 <= offset <= 100, "Offset must be between 0 and 100%"
            detector_obj = self._get_detector(detector)
            detector_obj.SetOffset(self._convert_from_percentage(detector_obj.GetOffsetRange(), offset))

        def set_segment_gain(self, detector: Detector, segment: Segment, gain: float):
            """Set the gain for a segment of detector DF4.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum
            segment : Segment
                Segment to get the gain from as an enum
            gain : float
                Gain as a percentage
            """
            assert 0 <= gain <= 100, "Gain must be between 0 and 100%"
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            assert type(segment) == Segment, "segment parameter must be of type Segment"
            detector = self._get_detector(detector)
            detector.Segments[segment.value].SetGain(self._convert_from_percentage(detector.GetGainRange(), gain))

        def set_segment_offset(self, detector: Detector, segment: Segment, offset: float):
            """Set the offset for a segment of detector DF4.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum
            segment : Segment
                Segment to get the offset from as an enum
            offset : float
                Offset as a percentage
            """
            assert 0 <= offset <= 100, "Offset must be between 0 and 100%"
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            assert type(segment) == Segment, "segment parameter must be of type Segment"
            detector = self._get_detector(detector)
            detector.Segments[segment.value].SetOffset(self._convert_from_percentage(detector.GetOffsetRange(), offset))

        def is_inserted(self, detector: Detector) -> bool:
            """Checks if a detector is inserted.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum

            Returns
            -------
            bool
                True if detector is inserted
            """
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            insertion_state = self._get_detector(detector).GetInsertionState()
            return insertion_state == IomAcquisitionCore.IomAcquisitionCoreLib.DetectorInsertionState_Inserted

        def is_retracted(self, detector: Detector) -> bool:
            """Checks if a detector is retracted.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum

            Returns
            -------
            bool
                True if detector is retracted
            """
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            retraction_state = self._get_detector(detector).GetInsertionState()
            return retraction_state == IomAcquisitionCore.IomAcquisitionCoreLib.DetectorInsertionState_Retracted

        def insert(self, detector: Detector):
            """Insert a detector.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum
            """
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            self._get_detector(detector).Insert()

        def retract(self, detector: Detector):
            """Retract a detector.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum.
            """
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            self._get_detector(detector).Retract()

        def is_present(self, detector: Detector) -> bool:
            """Check if a detector is present.

            Parameters
            ----------
            detector : Detector
                Name of the detector as an enum

            Returns
            -------
            bool
                True is detector is present
            """
            assert type(detector) == Detector, "detector parameter must be of type Detector"
            return self._get_detector(detector) is not None

        @staticmethod
        def _convert_to_percentage(detector_range, value):
            return (value - detector_range.begin) * 100 / (detector_range.end - detector_range.begin)

        @staticmethod
        def _convert_from_percentage(detector_range, value):
            return detector_range.begin + value * (detector_range.end - detector_range.begin) / 100

        def _get_detector(self, detector: Detector) -> IomAcquisitionStem.IomAcquisitionStemLib.IStemDetector:
            for stem_detector in self.interface.Stem:
                stem_detector_obj = stem_detector.QueryInterface(IomAcquisitionStem.IomAcquisitionStemLib.IStemDetector)
                if stem_detector_obj.Name != detector.value:
                    continue
                if detector in self.has_multi_segment:
                    stem_detector_obj = stem_detector.QueryInterface(
                        IomAcquisitionStem.IomAcquisitionStemLib.IMultiSegmentStemDetector
                    )
                return stem_detector_obj
            return None


class Beam:
    def __init__(self, interface):
        self.interface = interface.QueryInterface(IomAcquisitionScan.IomAcquisitionScanLib.IScan)

    def get_position(self) -> Tuple[float, float]:
        """Get the beam position.

        Returns
        -------
        Tuple[float, float]
            Tuple of floats giving respectively the horizontal and vertical location with range from 0 to 1
        """
        return PatternRenderer.spot_to_position(self.get_idle_scan_pattern())

    def set_position(self, x: float, y: float):
        """Sets the beam to the given location.

        Parameters
        ----------
        x : float
            horizontal location of beam ranging from 0 to 1
        y : float
            vertical location of beam ranging from 0 to 1
        """
        dwell_time = 1e-06  # value chosen empirically
        self.set_idle_scan_pattern(PatternRenderer.pattern_spot(x, y, dwell_time))

    def set_idle_scan_pattern(self, pattern: PatternRenderer.PatternRendererLib.IPatternSpot):
        self.interface.SetIdleScanPattern(pattern)

    def get_idle_scan_pattern(self) -> PatternRenderer.PatternRendererLib.IPatternSpot:
        return self.interface.GetIdleScanPattern()


class Configuration:
    def __init__(self, interface):
        self.interface = interface.QueryInterface(IomCommercialInfo.get_supported_interface())

    def is_stem_available(self) -> bool:
        """Check is stem mode is available.

        Returns
        -------
        bool
            True is stem mode is available
        """
        return self.interface.StemAvailable


class Instrument:
    def __init__(self):
        self.connection = Instrument4Connection()
        self.column = Column(self.connection.instrument.Column)
        self.stage = Column.Stage(self.connection.instrument.Column)
        self.holder = Column.Holder(self.connection.instrument.Column)
        self.beamstopper = Column.BeamStopper(self.connection.instrument.Column)
        self.vacuum = Vacuum(self.connection.instrument.Vacuum)
        self.beam = Beam(self.connection.instrument.Scan)
        self.source = Column.Source(self.connection.instrument.Column)
        self.optics = Column.Optics(self.connection.instrument.Column)
        self.stem_detector = Detectors.StemDetector(self.connection.instrument.Detectors)
        self.camera = Detectors.Camera(self.connection.instrument.Detectors)
        self.fluscreen = FluScreen(self.connection.instrument.FluScreens)
        self.configuration = Configuration(self.connection.instrument.CommercialInfo)

    def disconnect(self):
        self.connection.disconnect()
