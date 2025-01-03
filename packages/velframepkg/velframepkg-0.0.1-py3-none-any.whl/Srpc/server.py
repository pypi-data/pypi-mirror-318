# Copyright(c) 2022-2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

from rpyc.utils.server import ThreadedServer
from service import Service

if __name__ == "__main__":
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
        "sync_request_timeout": None,
    }
    # Use custom listener_timeout (10 seconds instead of 0.5 by default
    # Default timeout leads to rpc connexion error on some virtual machine
    server = ThreadedServer(Service, port=18000, protocol_config=config, listener_timeout=30)

    server.start()
