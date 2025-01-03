# Copyright(c) 2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import rpyc

RPC_CLIENT_CONFIG = {
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
    "sync_request_timeout": 1200,
}


class Client:
    """The rpyc client for the Installer application.

    Requires the rpyc server to be running on the system with Squish server.
    """

    def __init__(self, host: str):
        """Establishes the connection to the rpyc server.

        Parameters
        ----------
        host: the host name (or IP) for the system with the rpyc server
        """
        self.conn = rpyc.connect(host, 18000, config=RPC_CLIENT_CONFIG)

    def get_app(self):
        """Returns an instance of Installer running on rpyc server. The return type is deliberately missing because
        importing pywinauto (which the Installer class does) causes a ModuleNotFoundError if done outside of the virtual
        env (which Squish IDE does).

        Returns
        -------
        An Installer instance running on the same machine as the rpyc server, but able to be interacted
        with on the rpyc client machine.
        """
        return self.conn.root.get_installer()

    def close(self):
        """Closes the connection to the rpyc server."""
        self.conn.close()
