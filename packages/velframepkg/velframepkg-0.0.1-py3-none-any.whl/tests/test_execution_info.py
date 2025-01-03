# -*- coding: utf-8 -*-
# Copyright(c) 2021 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import sys

from common.execution_info import check_for_failures, record_test_selected, save_test_results
from mock import MagicMock, Mock, PropertyMock


def _no_failed_test_found():
    return {"failed_test_found": False}


def _failed_test_found():
    return {"failed_test_found": True}


def test_failed_test_found():
    # test setup
    context = MagicMock()
    squish_test = sys.modules["test"]
    squish_test.resultCount.return_value = 1
    user_data = PropertyMock(side_effect=_failed_test_found)
    type(context).userData = user_data

    # function under test
    check_for_failures(context)

    # expected test result
    squish_test.resultCount.assert_not_called()
    assert context.userData["failed_test_found"]


def test_no_failed_test_found():
    # test setup
    context = MagicMock()
    squish_test = sys.modules["test"]
    squish_test.resultCount.call_count = 0
    user_data = PropertyMock(side_effect=_no_failed_test_found)
    type(context).userData = user_data
    # all resultCount calls return 1 error so count only called once
    squish_test.resultCount.return_value = 1

    # function under test
    check_for_failures(context)

    # expected test result
    squish_test.resultCount.assert_called_once()


def test_no_failed_test_checks_all_types():
    # test setup
    context = MagicMock()
    squish_test = sys.modules["test"]
    squish_test.resultCount.call_count = 0
    user_data = PropertyMock(side_effect=_no_failed_test_found)
    type(context).userData = user_data
    # all resultCount calls return 0 error so count called for all types
    squish_test.resultCount.return_value = 0

    # function under test
    check_for_failures(context)

    # expected test result
    assert squish_test.resultCount.call_count == 3


def test_save_test_results_scenario_01():
    # test setup
    context = Mock()
    argument_parser = Mock()
    args = Mock()
    # Delete on "Test Passed" => Test Failed => Save results
    type(args).postProcessResult = PropertyMock(side_effect=["TestPassed"])
    type(context).userData = PropertyMock(side_effect=_failed_test_found)
    # assign property mock
    argument_parser.parse_arguments.return_value = (args, "")

    # function under test
    # expected test result
    assert save_test_results(context, argument_parser)


def test_save_test_results_scenario_02():
    # test setup
    context = Mock()
    argument_parser = Mock()
    args = Mock()
    # Delete on "Test Failed" => Test Passed => Save results
    type(args).postProcessResult = PropertyMock(side_effect=["TestFailed"])
    type(context).userData = PropertyMock(side_effect=_no_failed_test_found)
    # assign property mock
    argument_parser.parse_arguments.return_value = (args, "")

    # function under test
    # expected test result
    assert save_test_results(context, argument_parser)


def test_save_test_results_scenario_03():
    # test setup
    context = Mock()
    argument_parser = Mock()
    args = Mock()
    # Delete on "Never" => Test Passed => Save results
    type(args).postProcessResult = PropertyMock(side_effect=["Never"])
    type(context).userData = PropertyMock(side_effect=_no_failed_test_found)
    # assign property mock
    argument_parser.parse_arguments.return_value = (args, "")

    # function under test
    # expected test result
    assert save_test_results(context, argument_parser)


def test_save_test_results_scenario_04():
    # test setup
    context = Mock()
    argument_parser = Mock()
    args = Mock()

    # Delete on "Never" => Test Failed => Save results
    type(args).postProcessResult = PropertyMock(side_effect=["Never"])
    type(context).userData = PropertyMock(side_effect=_failed_test_found)
    # assign property mock
    argument_parser.parse_arguments.return_value = (args, "")

    # function under test
    # expected test result
    assert save_test_results(context, argument_parser)


def test_do_not_save_test_results_scenario_01():
    # test setup
    context = Mock()
    argument_parser = Mock()
    args = Mock()
    # Delete on "Test Passed" => Test Passed => NOT Save results
    type(args).postProcessResult = PropertyMock(side_effect=["TestPassed"])
    type(context).userData = PropertyMock(side_effect=_no_failed_test_found)
    # assign property mock
    argument_parser.parse_arguments.return_value = (args, "")

    # function under test
    # expected test result
    assert not save_test_results(context, argument_parser)


def test_do_not_save_test_results_scenario_02():
    # test setup
    context = Mock()
    argument_parser = Mock()
    args = Mock()
    # Delete on "Test Failed" => Test Failed => NOT Save results
    type(args).postProcessResult = PropertyMock(side_effect=["TestFailed"])
    type(context).userData = PropertyMock(side_effect=_failed_test_found)
    # assign property mock
    argument_parser.parse_arguments.return_value = (args, "")

    # function under test
    # expected test result
    assert not save_test_results(context, argument_parser)


def test_record_test_selected():
    # test setup
    argument_parser = Mock()
    args = Mock()
    argument_parser.parse_arguments.return_value = (args, "")
    type(args).record = PropertyMock(side_effect=["TRUE"])

    # function under test
    # expected test result
    assert record_test_selected(argument_parser)


def test_record_test_not_selected():
    # test setup
    argument_parser = Mock()
    args = Mock()
    argument_parser.parse_arguments.return_value = (args, "")
    # returning a value that is not convertible to true
    type(args).record = PropertyMock(side_effect=["TestPassed"])

    # function under test
    # expected test result
    assert not record_test_selected(argument_parser)
