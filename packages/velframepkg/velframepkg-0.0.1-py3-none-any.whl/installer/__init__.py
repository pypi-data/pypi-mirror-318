# Copyright(c) 2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
from common import execution_info
from Srpc import installer_client, remote_installer

remote_installer.ServerInstaller().install_server()
app_connection = installer_client.Client(host=execution_info.squish_host_name())

app = app_connection.get_app()
