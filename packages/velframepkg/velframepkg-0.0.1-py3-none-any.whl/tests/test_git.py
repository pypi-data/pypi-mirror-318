# -*- coding: utf-8 -*-
# Copyright(c) 2021 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

from common.git import Git
from mock import Mock


def test_get_stable_branch_name_with_maintenance_branch():
    # test setup
    connection = Mock()
    git = Git(connection)
    connection.getEnvironmentVariable.return_value = r"maint/img/check_for_branch"

    # function under test
    branch = git.get_stable_branch_name()

    # expected test result
    assert branch == r"maint/stable"


def test_get_stable_branch_name_with_uppercase_maintenance_branch():
    # test setup
    connection = Mock()
    git = Git(connection)
    connection.getEnvironmentVariable.return_value = r"Maint/img/check_for_branch"

    # function under test
    branch = git.get_stable_branch_name()

    # expected test result
    assert branch == r"maint/stable"


def test_get_stable_branch_name_with_feature_stable_branch():
    # test setup
    connection = Mock()
    git = Git(connection)
    connection.getEnvironmentVariable.return_value = r"feat/img/check_for_branch"

    # function under test
    branch = git.get_stable_branch_name()

    # expected test result
    assert branch == r"feat/stable"


def test_get_stable_branch_name_with_uppercase_feature_stable_branch():
    # test setup
    connection = Mock()
    git = Git(connection)
    connection.getEnvironmentVariable.return_value = r"FEAT/img/check_for_branch"

    # function under test
    branch = git.get_stable_branch_name()

    # expected test result
    assert branch == r"feat/stable"


def test_get_stable_branch_name_unknown_branch():
    # test setup
    connection = Mock()
    git = Git(connection)
    connection.getEnvironmentVariable.return_value = r"not/fnd/branch"

    # function under test
    branch = git.get_stable_branch_name()

    # expected test result
    assert branch == r"Unknown"
