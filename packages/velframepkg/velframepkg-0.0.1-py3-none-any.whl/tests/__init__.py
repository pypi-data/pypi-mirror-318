# -*- coding: utf-8 -*-
# Copyright(c) 2021 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import sys

from mock import MagicMock

sys.modules["test"] = MagicMock()
sys.modules["object"] = MagicMock()
sys.modules["squish"] = MagicMock()
sys.modules["remotesystem"] = MagicMock()
