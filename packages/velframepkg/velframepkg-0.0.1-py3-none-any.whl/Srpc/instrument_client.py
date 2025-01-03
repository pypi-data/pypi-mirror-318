# Copyright(c) 2022-2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import rpyc


class Client:
    def __init__(self, host):
        config = {
            "allow_all_attrs": True,
            "allow_pickle": True,
            "allow_getattr": True,
            "allow_setattr": True,
            "allow_delattr": True,
            "allow_exposed_attrs": True,
            "allow_public_attrs": True,
            "import_custom_exceptions": True,
            "instantiate_custom_exceptions": True,
            "instantiate_oldstyle_exceptions": True,
        }
        self.conn = rpyc.connect(host, 18000, config=config)

    def get_module(self):
        return self.conn.root.get_instrument_module()

    def get_instrument(self):
        return self.conn.root.get_instrument()

    def close(self):
        self.conn.close()


class LocalClient:
    def __init__(self):
        from Srpc.TemScripting import instrument

        self.instrument = instrument.Instrument()

    def get_module(self):
        from Srpc.TemScripting import instrument

        return instrument

    def get_instrument(self):
        return self.instrument


class MockClient:
    def __init__(self):
        from Srpc.TemScripting import instrument_mock

        self.instrument = instrument_mock.instrument

    def get_module(self):
        from Srpc.TemScripting import instrument_mock

        return instrument_mock

    def get_instrument(self):
        return self.instrument
