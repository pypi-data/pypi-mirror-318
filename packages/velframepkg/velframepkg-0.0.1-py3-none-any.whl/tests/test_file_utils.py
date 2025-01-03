# -*- coding: utf-8 -*-
# Copyright(c) 2021-2022 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

from common.file_utils import FileUtils
from mock import Mock


def _setup_test(exists: bool, stat: bool):
    connection = Mock()
    connection.exists.return_value = exists
    connection.stat.return_value = stat
    return connection


def test_directory_does_not_exists_scenario_01():
    # test setup
    file_utils = FileUtils(connection=_setup_test(False, False))

    # function under test
    # expected test result
    assert not file_utils.directory_exists(r"")


def test_directory_does_not_exist_scenario_02():
    # test setup
    file_utils = FileUtils(connection=_setup_test(False, True))

    # function under test
    # expected test result
    assert not file_utils.directory_exists(r"")


def test_directory_exists_but_not_a_directory():
    # test setup
    file_utils = FileUtils(connection=_setup_test(True, False))

    # function under test
    # expected test result
    assert not file_utils.directory_exists(r"")


def test_directory_exists_and_is_a_directory():
    # test setup
    file_utils = FileUtils(connection=_setup_test(True, True))

    # function under test
    # expected test result
    assert file_utils.directory_exists(r"")


def test_file_does_not_exist_scenario_01():
    # test setup
    file_utils = FileUtils(connection=_setup_test(False, False))

    # function under test
    # expected test result
    assert not file_utils.file_exists(r"")


def test_file_does_not_exist_scenario_02():
    # test setup
    file_utils = FileUtils(connection=_setup_test(False, True))

    # function under test
    # expected test result
    assert not file_utils.file_exists(r"")


def test_file_exist_but_not_a_file():
    # test setup
    file_utils = FileUtils(connection=_setup_test(True, False))

    # function under test
    # expected test result
    assert not file_utils.file_exists(r"")


def test_file_exist_and_file():
    # test setup
    file_utils = FileUtils(connection=_setup_test(True, True))

    # function under test
    # expected test result
    assert file_utils.file_exists(r"")


def test_create_directory_on_already_existing_directory():
    # test setup
    path_name = r"c:\imaginary_path"
    # directory already exists
    connection = _setup_test(True, True)
    file_utils = FileUtils(connection=connection)

    # function under test
    file_utils.create_directory(path_name)

    # expected test result
    connection.createPath.assert_not_called()


def test_create_directory():
    # test setup
    path_name = r"c:\imaginary_path"
    connection = Mock()
    connection.exists.side_effect = [False, True]
    connection.stat.return_value = True
    file_utils = FileUtils(connection=connection)
    file_utils.create_directory(path_name)

    # function under test
    connection.createPath.assert_called_once()

    # expected test result
    connection.createPath.called_with(path_name)


def test_update_file_creation_to_now_succeeded():
    # test setup
    connection = Mock()
    connection.execute.return_value = (0, "std_out", "std_err")
    file_utils = FileUtils(connection=connection)

    # function under test
    # expected test result
    assert file_utils.update_file_creation_to_now(r"c:\imaginary\file")


def test_update_file_creation_to_now_failed():
    # test setup
    connection = Mock()
    connection.execute.return_value = (1, "std_out", "std_err")
    file_utils = FileUtils(connection=connection)

    # function under test
    # expected test result
    assert not file_utils.update_file_creation_to_now(r"c:\imaginary\file")


def test_delete_file():
    # function under test
    # expected test result
    assert FileUtils(Mock()).delete_file(r"c:\imaginary\file") is None


def test_copy_file_do_not_overwrite_target():
    # test setup
    connection = _setup_test(True, True)
    file_utils = FileUtils(connection=connection)

    # function under test
    file_utils.copy_file(r"c:\imaginary\file\source", r"c:\imaginary\file\destination", False)

    # expected test result
    connection.deleteFile.assert_not_called()


def test_copy_file_non_existing_target():
    # test setup
    connection = Mock()
    connection.exists.side_effect = [False, True]
    connection.stat.return_value = True

    file_utils = FileUtils(connection=connection)

    # function under test
    file_utils.copy_file(r"c:\imaginary\file\source", r"c:\imaginary\file\destination", True)

    # expected test result
    connection.deleteFile.assert_not_called()
    connection.copy.assert_called_with(r"c:\imaginary\file\source", r"c:\imaginary\file\destination")


def test_copy_file_existing_target_overwrite():
    # test setup
    connection = _setup_test(True, True)
    file_utils = FileUtils(connection=connection)

    # function under test
    file_utils.copy_file(r"c:\imaginary\file\source", r"c:\imaginary\file\destination", True)

    # expected test result
    connection.deleteFile.assert_called_once()


def test_get_creation_time():
    # function under test
    # expected test result
    FileUtils(Mock()).get_creation_date(r"c:\imaginary\file")


def test_convert_wild_card_to_regex_regular_wildcard():
    # function under test
    # expected test result
    assert FileUtils.convert_wild_card_to_regex("*24*.mkv") == r"^.*24.*\.mkv$"


def test_convert_wild_card_to_regex_all_files():
    # function under test
    # expected test result
    assert FileUtils.convert_wild_card_to_regex("*.*") == r"^.*\..*$"


def test_convert_wild_card_to_regex_no_extension():
    # function under test
    # expected test result
    assert FileUtils.convert_wild_card_to_regex("*.") == r"^.*\.$"


def test_convert_wild_card_to_regex_one_char_files():
    # function under test
    # expected test result
    assert FileUtils.convert_wild_card_to_regex(".") == r"^\.$"


def test_convert_wild_card_to_regex_no_selection():
    # function under test
    # expected test result
    assert FileUtils.convert_wild_card_to_regex("") == r"^$"


def test_convert_wild_card_to_regex_wildcard_and_chars():
    # function under test
    # expected test result
    assert FileUtils.convert_wild_card_to_regex("*f?.?oo") == r"^.*f.\..oo$"


def test_convert_wild_card_to_regex_multiple_wildcards_and_chars():
    # function under test
    # expected test result
    assert FileUtils.convert_wild_card_to_regex("*.*.*.*") == r"^.*\..*\..*\..*$"


def test_get_directory_list_directory_does_not_exist():
    # test setup
    connection = _setup_test(False, False)
    file_utils = FileUtils(connection=connection)

    # function under test
    directory_list = file_utils.get_directories(r"c:\imaginary_directory")

    # expected test result
    assert len(directory_list) == 0
    connection.exists.assert_called_once()
    connection.stat.assert_not_called()
    connection.listFiles.assert_not_called()


def test_get_directory_list_no_directories():
    # test setup
    connection = _setup_test(True, True)
    connection.listFiles.return_value = []
    file_utils = FileUtils(connection=connection)

    # function under test
    directory_list = file_utils.get_directories(r"c:\imaginary_directory")

    # expected test result
    assert len(directory_list) == 0
    connection.stat.assert_called_once()


def test_get_directory_list_directories_found():
    # test setup
    connection = _setup_test(True, True)
    connection.listFiles.return_value = ["directory_01", "directory_02", "directory_03"]
    file_utils = FileUtils(connection=connection)

    # function under test
    directory_list = file_utils.get_directories(r"c:\imaginary_directory")

    # expected test result
    assert directory_list == connection.listFiles.return_value
    assert connection.stat.call_count == 4


def test_get_files_directory_does_not_exist():
    # test setup
    connection = _setup_test(False, False)
    file_utils = FileUtils(connection=connection)

    # function under test
    file_list = file_utils.get_directory_content(r"c:\imaginary_directory")

    # expected test result
    assert len(file_list) == 0
    connection.listFiles.assert_not_called()


def test_get_files_empty_directory():
    # test setup
    connection = _setup_test(True, True)
    file_utils = FileUtils(connection=connection)
    connection.listFiles.return_value = []

    # function under test
    file_list = file_utils.get_directory_content(r"c:\imaginary_directory")

    # expected test result
    assert len(file_list) == 0
    connection.stat.assert_called_once()
    connection.listFiles.assert_called_once()


def _fill_file_list():
    return [
        "2021-05-25 09-34-24.mkv",
        "2021-05-25 09-47-48.mkv",
        "2021-05-25 10-13-07.mkv",
        "2021-05-25 11-09-35.mkv",
        "2021-05-25 14-08-26.mkv",
        "2021-05-25 14-18-12.mkv",
        "2021-05-25 14-21-48.mkv",
    ]


def test_get_files_all_files():
    # test setup
    connection = _setup_test(True, True)
    connection.listFiles.return_value = _fill_file_list()
    file_utils = FileUtils(connection=connection)

    # function under test
    file_list = file_utils.get_directory_content(r"c:\imaginary_directory")

    # expected test result
    assert len(file_list) == len(_fill_file_list())
    assert file_list[0] == r"c:\imaginary_directory\2021-05-25 09-34-24.mkv"


def test_get_files_filter_one_file():
    # test setup
    connection = _setup_test(True, True)
    connection.listFiles.return_value = _fill_file_list()
    file_utils = FileUtils(connection=connection)

    # function under test
    file_list = file_utils.get_directory_content(r"c:\imaginary_directory", "*24*.mkv")

    # expected test result
    assert file_list == [r"c:\imaginary_directory\2021-05-25 09-34-24.mkv"]


def test_get_files_filter_all_files_with_25():
    # test setup
    connection = _setup_test(True, True)
    connection.listFiles.return_value = _fill_file_list()
    file_utils = FileUtils(connection=connection)

    # function under test
    file_list = file_utils.get_directory_content(r"c:\imaginary_directory", "*25*.mkv")

    # expected test result
    assert len(file_list) == len(_fill_file_list())


def test_get_files_filter_two_files():
    # test setup
    connection = _setup_test(True, True)
    connection.listFiles.return_value = _fill_file_list()
    file_utils = FileUtils(connection=connection)

    # function under test
    file_list = file_utils.get_directory_content(r"c:\imaginary_directory", "*-48*.mkv")

    # expected test result
    assert len(file_list) == 2
    assert file_list[0] == r"c:\imaginary_directory\2021-05-25 09-47-48.mkv"


def test_get_files_filter_all_files():
    # test setup
    connection = _setup_test(True, True)
    connection.listFiles.return_value = _fill_file_list()
    file_utils = FileUtils(connection=connection)

    # function under test
    file_list = file_utils.get_directory_content(r"c:\imaginary_directory", "*")

    # expected test result
    assert len(file_list) == len(_fill_file_list())


def test_get_files_filter_one_file_with_char_and_wildcard_filter():
    # test setup
    connection = _setup_test(True, True)
    connection.listFiles.return_value = _fill_file_list()
    file_utils = FileUtils(connection=connection)

    # function under test
    file_list = file_utils.get_directory_content(r"c:\imaginary_directory", "*-?4-*")

    # expected test result
    assert len(file_list) == 1
    assert file_list[0] == r"c:\imaginary_directory\2021-05-25 09-34-24.mkv"


def test_remove_invalid_filesystem_characters_some_invalid():
    # function under test
    # expected test result
    assert FileUtils.remove_invalid_filename_characters(r"fdkljf23A@fd?//\\[]*.") == "fdkljf23Afd"


def test_remove_invalid_filesystem_characters_all_invalid():
    # function under test
    # expected test result
    assert FileUtils.remove_invalid_filename_characters(r"-:@%^&<>|'`,;=()!\[\]\"\"\"\".*?\\\/") == ""


def test_remove_invalid_filesystem_characters_all_invalid_per_char():
    # function under test
    # expected test result
    for char in r"-:@%^&<>|'`,;=()!\[\]\"\"\"\".*?\\\/":
        assert FileUtils.remove_invalid_filename_characters(char) == ""
