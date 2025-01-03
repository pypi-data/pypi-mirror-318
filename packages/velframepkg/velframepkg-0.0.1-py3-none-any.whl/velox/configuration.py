# Copyright(c) 2020-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import re
import test

from velox.registry_utils import RegistryContent


class TypeTemProductVersion:
    def __init__(self, microscope_type: str, product_version: str, tem_version: str):
        """Initialization of Menu instance.

        Parameters
        ----------
        microscope_type: String with the microscope type
        product_version: Product version of the microscope
        tem_version: Matching tem version
        """
        self.microscope_type = microscope_type
        self.product_version = product_version
        self.tem_version = tem_version


class TypeTemProductVersions:
    _type_tem_product_versions = [
        TypeTemProductVersion("Talos", "1.15", "6.15"),
        TypeTemProductVersion("Talos", "1.14", "6.14"),
        TypeTemProductVersion("Talos", "1.13", "6.13"),
        TypeTemProductVersion("Talos", "1.12", "6.12"),
        TypeTemProductVersion("Talos", "1.11", "6.11"),
        TypeTemProductVersion("Talos", "1.10", "6.10"),
        TypeTemProductVersion("Talos", "1.9", "6.9"),
        TypeTemProductVersion("Talos", "1.8", "6.8"),
        TypeTemProductVersion("Talos", "1.7", "6.7"),
        TypeTemProductVersion("Talos", "1.6", "6.6"),
        TypeTemProductVersion("Talos", "1.5", "6.5"),
        TypeTemProductVersion("Talos", "1.4", "6.4"),
        TypeTemProductVersion("Talos", "2.0", "7.0"),
        TypeTemProductVersion("Talos", "2.1", "7.1"),
        TypeTemProductVersion("Talos", "2.2", "7.2"),
        TypeTemProductVersion("Talos", "2.3", "7.3"),
        TypeTemProductVersion("Talos", "2.4", "7.4"),
        TypeTemProductVersion("Talos", "2.5", "7.5"),
        TypeTemProductVersion("Talos", "2.6", "7.6"),
        TypeTemProductVersion("Talos", "2.7", "7.7"),
        TypeTemProductVersion("Talos", "2.11", "7.11"),
        TypeTemProductVersion("Talos", "2.12", "7.12"),
        TypeTemProductVersion("Talos", "2.13", "7.13"),
        TypeTemProductVersion("Talos", "2.14", "7.14"),
        TypeTemProductVersion("Talos", "2.15", "7.15"),
        TypeTemProductVersion("Titan", "2.15", "6.15"),
        TypeTemProductVersion("Titan", "2.14", "6.14"),
        TypeTemProductVersion("Titan", "2.13", "6.13"),
        TypeTemProductVersion("Titan", "2.12", "6.12"),
        TypeTemProductVersion("Titan", "2.11", "6.11"),
        TypeTemProductVersion("Titan", "2.10", "6.10"),
        TypeTemProductVersion("Titan", "2.9", "6.9"),
        TypeTemProductVersion("Titan", "2.8", "6.8"),
        TypeTemProductVersion("Titan", "2.7", "6.7"),
        TypeTemProductVersion("Titan", "2.6", "6.6"),
        TypeTemProductVersion("Titan", "2.5", "6.5"),
        TypeTemProductVersion("Titan", "2.4", "6.4"),
        TypeTemProductVersion("Titan", "3.0", "7.0"),
        TypeTemProductVersion("Titan", "3.1", "7.1"),
        TypeTemProductVersion("Titan", "3.2", "7.2"),
        TypeTemProductVersion("Titan", "3.3", "7.3"),
        TypeTemProductVersion("Titan", "3.4", "7.4"),
        TypeTemProductVersion("Titan", "3.5", "7.5"),
        TypeTemProductVersion("Titan", "3.6", "7.6"),
        TypeTemProductVersion("Titan", "3.7", "7.7"),
        TypeTemProductVersion("Titan", "3.11", "7.11"),
        TypeTemProductVersion("Tecnai", "5.15", "6.15"),
        TypeTemProductVersion("Tecnai", "5.14", "6.14"),
        TypeTemProductVersion("Tecnai", "5.13", "6.13"),
        TypeTemProductVersion("Tecnai", "5.12", "6.12"),
        TypeTemProductVersion("Tecnai", "5.11", "6.11"),
        TypeTemProductVersion("Tecnai", "5.10", "6.10"),
        TypeTemProductVersion("Tecnai", "5.9", "6.9"),
        TypeTemProductVersion("Tecnai", "5.8", "6.8"),
        TypeTemProductVersion("Tecnai", "5.7", "6.7"),
        TypeTemProductVersion("Tecnai", "5.6", "6.6"),
        TypeTemProductVersion("Tecnai", "5.5", "6.5"),
        TypeTemProductVersion("Tecnai", "5.4", "6.4"),
    ]

    def get_tem_server_version(self, microscope_type: str, product_version: str) -> str:
        """Searches for the TEM server version of the given microscope type and product version and return its version
        if found otherwise "Unknown" is returned.

        Parameters
        ----------
        microscope_type: String with the microscope type
        product_version: Product version of the microscope

        Returns
        -------
        Tem server version if found else "Unknown" is returned
        """
        # only use the first 2 parts (ie 1.5.1 -> 1.5)
        product_version_arr = product_version.split(".")
        product_version = ".".join([product_version_arr[0], product_version_arr[1]])
        # go through list and get version
        retval = "Unknown"
        server_version = [
            type_tem_product_version
            for type_tem_product_version in self._type_tem_product_versions
            if type_tem_product_version.microscope_type == microscope_type
            and type_tem_product_version.product_version == product_version
        ]
        if len(server_version) > 0:
            retval = server_version[0].tem_version
        return retval


class MicroscopeConfiguration:

    _config = RegistryContent(r"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Fei\Configuration")
    _tem = RegistryContent(r"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Fei\BrickBox\Configurations\Tem")
    _vacuum = RegistryContent(
        r"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Fei\BrickBox\Configurations\TEM\Default\MdlVacuum\RuntimeSettings"
    )

    @property
    def timeout_pump_airlock_correct(self) -> bool:
        """Checks if HolderPumpAirlock timeout is correct, if value not found defaulting to True.

        Returns
        -------
        True if simulated and equal to 3 seconds, True if value not found
        """
        retval = False
        if self.simulated:
            if self._vacuum.exists:
                retval = "HolderPumpAirlock" in self._vacuum.dict and self._vacuum.dict["HolderPumpAirlock"] == "0x3"
            else:
                test.warning(
                    "Unable to get the HolderPumpAirlock value. Be aware that vacuum can be an issue after holder"
                    " insert."
                )
                retval = True
        test.log(f"timeout_pump_airlock_correct returned {retval}")
        return retval

    @property
    def simulated(self) -> bool:
        """Checks if Velox is running on a simulator or a real system.

        Returns
        -------
        True if it's a simulated environment
        """
        retval = "SimulationMode" in self._tem.dict and self._tem.dict["SimulationMode"] == "0x2"
        test.log(f"simulated returned {retval}")
        return retval

    @property
    def microscope_type(self) -> str:
        """Checks type of microscope.

        Returns
        -------
        Type as a string Titan/Talos
        """
        retval = (
            "Talos"
            if "Microscope Type" in self._config.dict and "Talos" in self._config.dict["Microscope Type"]
            else "Titan"
        )
        test.log(f"microscope_type returned {retval}")
        return retval

    @property
    def tem_base_folder(self) -> str:
        """Returns base folder which is Tecnai or Titan.

        Returns
        -------
        Name only as base folder
        """
        retval = (
            "Tecnai"
            if "Microscope Type" in self._config.dict and "Talos" in self._config.dict["Microscope Type"]
            else "Titan"
        )
        test.log(f"tem_base_folder returned {retval}")
        return retval

    @property
    def tem_version(self) -> str:
        """Returns the current tem-server version.

        Returns
        -------
        Version as a string
        """
        retval = (
            TypeTemProductVersions().get_tem_server_version(self.microscope_type, self._config.dict["Build Version"])
            if "Build Version" in self._config.dict
            else "Unknown"
        )
        test.log(f"tem_version returned {retval}")
        return retval

    @property
    def tem_version_raw(self) -> str:
        """Returns the raw tem-server version.

        Returns
        -------
        Version as a string
        """
        retval = (
            f"{self._config.dict['Build Version']}.{self._config.dict['Build Number']}"
            if "Build Version" in self._config.dict and "Build Number" in self._config.dict
            else "Unknown"
        )
        return retval

    def tem_version_at_least(self, tem_version) -> bool:
        """Checks if the current tem-server version is at least the given version.

        Parameters
        ----------
        tem_version: Least version to check for as a string ('6.6')

        Returns
        -------
        True when it is at least the given version
        """
        return self.tem_version >= tem_version

    @property
    def has_stem(self) -> bool:
        """Returns if the microscope has STEM capabilities.

        Returns
        -------
        True when the microscope has STEM otherwise False
        """
        retval = "STEM" in self._config.dict and self._config.dict["STEM"] == "True"
        test.log(f"has_stem returned {retval}")
        return retval

    @property
    def has_ngstem(self) -> bool:
        """Returns if the microscope has NGSTEM capabilities.

        Returns
        -------
        True when the microscope has NGSTEM otherwise False
        """
        if self.has_stem:
            retval = (
                "BF-S/DF-S Retractable" in self._config.dict and self._config.dict["BF-S/DF-S Retractable"] == "True"
            )
            test.log(f"has_ngstem returned {retval}")
            return retval
        else:
            return False

    @property
    def stem_detectors(self) -> list:
        """Checks in the configuration for the available stem detectors.

        Returns
        -------
        Returns the list of available STEM detectors as a string array
        """
        retval = list()
        if self.has_stem:
            values = self._config.dict
            if ("BF/DF Retractable" in values) and (values["BF/DF Retractable"] == "True"):
                retval.append("DF2")
                retval.append("DF4")
                retval.append("BF")
            elif ("BF-S/DF-S Retractable" in values) and (values["BF-S/DF-S Retractable"] == "True"):
                retval.append("DF-S")
                retval.append("BF-S")
                retval.append("DF-O")
                retval.append("DF-I")
            if ("HAADF" in values) and (values["HAADF"] == "True"):
                retval.append("HAADF")
        test.log(f"stem_detectors returned {retval}")
        return retval

    @property
    def has_eds(self) -> bool:
        """Returns if the microscope has EDS capabilities.

        Returns
        -------
        True when the microscope has EDS otherwise False
        """
        retval = self.eds_detector_type != "Unknown"
        test.log(f"has_eds returned {retval}")
        return retval

    @property
    def eds_detector_type(self) -> str:
        """Returns the type of eds detector.

        Returns
        -------
        String stating the detector type 'superx-g1', 'superx-g2' or 'dualx'.
        If no eds detector exists it will return an empty string
        """
        values = self._config.dict
        retval = "Unknown"
        if "SuperX Detector" in values:
            if "G1" in values["SuperX Detector"]:
                retval = "superx-g1"
            elif "G2" in values["SuperX Detector"]:
                retval = "superx-g2"
            elif "DualX" in values["SuperX Detector"]:
                retval = "dualx"
            elif "SingleX" in values["SuperX Detector"]:
                retval = "singlex"
        test.log(f"eds_detector_type returned {retval}")
        return retval

    @property
    def is_superx_g2(self) -> bool:
        """Returns if the type of eds detector is a SuperX G2.

        Returns
        -------
        True if it's a SuperX G2 detector
        """
        return self.eds_detector_type == "superx-g2"

    @property
    def has_camera(self) -> bool:
        """Returns if the microscope has Camera capabilities.

        Returns
        -------
        True when the microscope has Camera otherwise False
        """
        retval = self.has_ceta1 or self.has_ceta2 or self.has_falcon
        test.log(f"has_camera returned {retval}")
        return retval

    @property
    def camera_type(self) -> str:
        """Returns the type of camera.

        Returns
        -------
        String stating the detector type 'ceta1', 'ceta'. If no camera exists it will return an empty string
        """
        retval = ""
        values = self._config.dict
        if "BM-Falcon" in values and not set(["Falcon-3", "Falcon-4"]).isdisjoint(values["BM-Falcon"]):
            retval = "falcon"
        elif self.ceta_type != "":
            retval = self.ceta_type
        test.log(f"camera_type returned {retval}")
        return retval

    @property
    def ceta_type(self) -> str:
        """Returns the type (1 or 2) of ceta camera.

        Returns
        -------
        String stating the ceta camera type 'ceta1' or 'ceta2'. If no ceta camera exists it will return an empty string
        """
        retval = ""
        values = self._config.dict
        if "BM-Ceta" in values:
            has_speed_enhancement = (
                "BM-Ceta Speed Enhancement" in values and values["BM-Ceta Speed Enhancement"] == "True"
            )
            has_16m = "Ceta 16M" in values["BM-Ceta"]
            has_ceta2 = "Ceta 2" in values["BM-Ceta"] or "Ceta S" in values["BM-Ceta"]
            if has_16m and not has_speed_enhancement:
                retval = "ceta1"
            elif has_ceta2 or (has_16m and has_speed_enhancement):
                retval = "ceta2"
        test.log(f"ceta_type returned {retval}")
        return retval

    @property
    def has_falcon(self) -> bool:
        """Returns True if the system has a falcon.

        Returns
        -------
        True if it has a falcon
        """
        values = self._config.dict
        retval = "BM-Falcon" in values and not set(["Falcon-3", "Falcon-4"]).isdisjoint(values["BM-Falcon"])
        test.log(f"has_falcon returned {retval}")
        return retval

    @property
    def has_smcb(self) -> bool:
        """Returns True if the system has a SMCB motion controller.

        Returns
        -------
        True if it has a SMCB motion controller
        """
        values = self._config.dict
        retval = "CompuStage Motion Controller" in values and "SMCB" in values["CompuStage Motion Controller"]
        test.log(f"has_smcb returned {retval}")
        return retval

    @property
    def has_ceta(self) -> bool:
        """Returns if the system has a ceta camera.

        Returns
        -------
        True if it has a ceta camera
        """
        retval = self.has_ceta1 or self.has_ceta2
        test.log(f"has_ceta returned {retval}")
        return retval

    @property
    def has_ceta1(self) -> bool:
        """Returns if the system has a ceta1.

        Returns
        -------
        True if it has a ceta1
        """
        values = self._config.dict

        has_bm_ceta = "BM-Ceta" in values
        if has_bm_ceta:
            has_16m = "Ceta 16M" in values["BM-Ceta"]
            has_speed_enhancement = (
                "BM-Ceta Speed Enhancement" in values and values["BM-Ceta Speed Enhancement"] == "True"
            )

        retval = has_bm_ceta and has_16m and not has_speed_enhancement
        test.log(f"has_ceta1 returned {retval}")
        return retval

    @property
    def has_ceta2(self) -> bool:
        """Returns if the system has a ceta2.

        Returns
        -------
        True if it has a ceta2
        """
        values = self._config.dict

        has_bm_ceta = "BM-Ceta" in values
        if has_bm_ceta:
            has_speed_enhancement = (
                "BM-Ceta Speed Enhancement" in values and values["BM-Ceta Speed Enhancement"] == "True"
            )
            has_16m = "Ceta 16M" in values["BM-Ceta"]
            has_ceta2 = "Ceta 2" in values["BM-Ceta"] or "Ceta S" in values["BM-Ceta"]

        retval = has_ceta2 or (has_16m and has_speed_enhancement)
        test.log(f"has_ceta2 returned {retval}")
        return retval

    @property
    def has_multiple_camera(self) -> bool:
        """Returns True if there is more then one camera.

        Returns
        -------
        True if there is more then one camera
        """
        retval = self.has_falcon and self.has_ceta
        test.log(f"has_multiple_camera returned {retval}")
        return retval

    @property
    def has_imaging_filter(self) -> bool:
        """Returns True if there is not none value for imaging filter.

        Returns
        -------
        True if there is not none value for imaging filter
        """
        values = self._config.dict
        retval = "Imaging Filter" in values and "FBB" in values["Imaging Filter"]
        test.log(f"has_imaging_filter returned {retval}")
        return retval

    @property
    def has_single_tilt(self) -> bool:
        """Check if the microscope has a Single Tilt Holder.

        Returns
        -------
        True when the microscope has a Single Tilt Holder
        """
        retval = False
        for holder in ["Single Tilt Holder", "Single Tilt Mk2 Holder"]:
            if holder in self._config.dict and "True" in self._config.dict[holder]:
                retval = True
                break
        test.log(f"has_single_tilt returned {retval}")
        return retval

    @property
    def has_double_tilt(self) -> bool:
        """Check if the microscope has a Double Tilt Holder.

        Returns
        -------
        True when the microscope has a Double Tilt Holder
        """
        retval = False
        for holder in ["Double Tilt Holder", "Double Tilt Mk2 Holder"]:
            if holder in self._config.dict and "True" in self._config.dict[holder]:
                retval = True
                break
        test.log(f"has_double_tilt returned {retval}")
        return retval

    @property
    def lab6(self) -> bool:
        """Check if the microscope is a Lab6 machine.

        Returns
        -------
        True when the microscope is Lab6
        """
        retval = "Microscope Type" in self._config.dict and "Talos L120C" in self._config.dict["Microscope Type"]
        test.log(f"lab6 returned {retval}")
        return retval

    def _has_iom2_based_on_tem_version(self) -> list:
        """Checks in the configuration for the available stem detectors.

        Returns
        -------
        Returns the list of available STEM detectors as a string array
        """
        iom2_tem_versions_re = "^7.[0-6]"
        return self.tem_version.startswith("6.") or re.search(iom2_tem_versions_re, self.tem_version) is not None

    def has_iom_2(self) -> bool:
        """Check if the microscope has an IOM2 interface.

        Returns
        -------
        True when the microscope has this interface
        """
        retval = self._has_iom2_based_on_tem_version()
        test.log(f"has_iom_2 returned {retval}")
        return retval

    def has_iom_3(self) -> bool:
        """Check if the microscope has an IOM3 interface.

        Returns
        -------
        True when the microscope has this interface
        """
        # iom3 conditions are the same as iom2 conditions
        return self.has_iom_2()

    def export_config_as_file(self, file_path: str) -> bool:
        """Creates a file that contains the TEM server configuration.

        Parameters
        ----------
        file_path: path to a file that containing the configuration

        Returns
        -------
        True if configuration was successfully exported, False otherwise
        """
        if not self._config.dict:
            return False

        with open(file_path, "w") as config_file:
            for key in sorted(self._config.dict, key=lambda s: s.lower()):
                config_file.write(f"{key} : {self._config.dict[key]}\n")

        return True
