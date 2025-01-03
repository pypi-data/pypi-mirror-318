# Copyright(c) 2022-2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import sys

from common import execution_info
from Srpc import instrument_client, remote_installer

if execution_info.is_online_system():
    if execution_info.is_local_run():
        remote_installer.ServerInstaller().stop_server()
        instrument_connection = instrument_client.LocalClient()
    else:
        remote_installer.ServerInstaller().install_server()
        instrument_connection = instrument_client.Client(host=execution_info.squish_host_name())
else:
    instrument_connection = instrument_client.MockClient()

# part below makes it possible to call method without the namespace
this_module = sys.modules[__name__]
for key, value in instrument_connection.get_module().__dict__.items():
    this_module.__dict__[key] = value

instrument = instrument_connection.get_instrument()
