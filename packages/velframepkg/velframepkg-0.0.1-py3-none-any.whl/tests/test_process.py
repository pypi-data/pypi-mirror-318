# -*- coding: utf-8 -*-
# Copyright(c) 2021 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

from common.process import Process
from mock import Mock


def _get_process_list():
    return (
        '"Image Name","PID","Session Name","Session#","Mem Usage"\n'
        + '"System Idle Process","0","Services","0","24 K"\n'
        + '"System","4","Services","0","4,080 K"\n'
        + '"smss.exe","468","Services","0","384 K"\n'
        + '"csrss.exe","756","Services","0","2,540 K"\n'
        + '"wininit.exe","840","Services","0","528 K"\n'
        + '"csrss.exe","848","Console","1","18,780 K"\n'
        + '"services.exe","908","Services","0","15,752 K"\n'
        + '"lsass.exe","920","Services","0","26,148 K"\n'
        + '"lsm.exe","928","Services","0","5,872 K"\n'
        + '"winlogon.exe","172","Console","1","2,920 K"\n'
        + '"svchost.exe","636","Services","0","7,620 K"\n'
        + '"svchost.exe","796","Services","0","14,108 K"\n'
        + '"svchost.exe","1032","Services","0","33,488 K"\n'
        + '"svchost.exe","1104","Services","0","6,104 K"\n'
        + '"svchost.exe","1136","Services","0","21,468 K"\n'
        + '"svchost.exe","1164","Services","0","126,984 K"\n'
        + '"svchost.exe","1280","Services","0","22,008 K"\n'
        + '"dsAccessService.exe","1564","Services","0","1,992 K"\n'
        + '"tasklist.exe","35484","Console","1","7,476 K"\n'
    )


def test_get_process_ids_failed():
    # test setup
    connection = Mock()
    process = Process(connection)
    connection.execute.return_value = (1, "stdout", "stderr")

    # function under test
    process_list = process.get_process_ids("Velox")

    # expected test result
    assert len(process_list) == 0


def test_get_process_ids_lower_case():
    # test setup
    connection = Mock()
    process = Process(connection)
    connection.execute.return_value = (0, _get_process_list(), "")

    # function under test
    process_list = process.get_process_ids("svchost")

    # expected test result
    assert process_list == [636, 796, 1032, 1104, 1136, 1164, 1280]


def test_get_process_ids_upper_case():
    # test setup
    connection = Mock()
    process = Process(connection)
    connection.execute.return_value = (0, _get_process_list(), "")

    # function under test
    process_list = process.get_process_ids("SVCHOST")

    # expected test result
    assert process_list == [636, 796, 1032, 1104, 1136, 1164, 1280]


def test_get_process_ids_not_found():
    # test setup
    connection = Mock()
    process = Process(connection)
    connection.execute.return_value = (0, _get_process_list(), "")

    # function under test
    process_list = process.get_process_ids("NOT_CORRECT")

    # expected test result
    assert process_list == []
