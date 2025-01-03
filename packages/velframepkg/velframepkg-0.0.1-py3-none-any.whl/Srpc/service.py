# Copyright(c) 2022-2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import rpyc
from apps.external_access import ExternalAccessUI
from apps.mdl_stage_ui import MdlStageUI
from TemScripting import instrument


class Service(rpyc.Service):
    def __init__(self):
        self.instrument = instrument.Instrument()
        self.mdl_stage_ui = MdlStageUI()
        self.external_access_ui = ExternalAccessUI()

    @staticmethod
    def exposed_get_instrument_module():
        return instrument

    def exposed_get_instrument(self):
        return self.instrument

    def exposed_get_mdl_stage_ui(self):
        return self.mdl_stage_ui

    def exposed_get_external_access_ui(self):
        return self.external_access_ui
