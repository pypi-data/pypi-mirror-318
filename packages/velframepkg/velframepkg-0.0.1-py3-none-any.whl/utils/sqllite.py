# Copyright(c) 2023-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

import os
import sqlite3
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import List

DB_PATH = r"//veloxfileserver/velox/Integration/VeloxTests/UITestlog.db"

SELECT_LAST_N_TESTS_QUERY = """
SELECT
  *
FROM
  UITestLog ul
WHERE
  Machine = ?
ORDER BY
  EndTime DESC
LIMIT
  ?;
"""

DB_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

# Keys are the hostname of the MPCs. Values are the corresponding field
# 'Machine' in the UI test log database
DB_MACHINE_NAME_MAP = {
    "NLEIN-VELOX-01": "VELOX-01",
    "NLEIN-VELOX-02": "VELOX-02",
    "NLEIN-VELOX-03": "VELOX-03",
    "NLEIN-VELOX-04": "VELOX-04",
    "NLEIN-VELOX-05": "VELOX-05",
    "NLEIN-VELOX-06": "VELOX-06",
    "NLEIN-VELOX-21": "VELOX-21",
    "NLEIN-VELOX-22": "VELOX-22",
    "NLEIN-VELOX-23": "VELOX-23",
    "NLEIN-VELOX-24": "VELOX-24",
    "NLEIN-VELOX-25": "VELOX-25",
    "VELOX-TST01": "Win10-01",
    "VELOX-TST02": "Win10-02",
    "VELOX-TST03": "Win10-03",
    "VELOX-TST04": "Win10-04",
    "VELOX-TST05": "Win10-05",
    "VELOX-TST06": "Win10-06",
    "VELOX-TST07": "Win10-07",
    "VELOX-TST08": "Win10-08",
    "NLEIN-VELOX-111": "Win11-01",
    "NLEIN-VELOX-112": "Win11-02",
    "NLEIN-VELOX-113": "Win11-03",
    "NLEIN-VELOX-114": "Win11-04",
    "NLEIN-VELOX-115": "Win11-05",
}


@dataclass
class UITestLogEntry:
    """An instance of this class represents an entry in our UITestLog database."""

    id: int
    test_suite: str
    test_case: str
    start_time: datetime
    end_time: datetime
    branch: str
    machine: str
    job: str
    status: str

    def __init__(self, db_result: tuple):
        """Creates an instance of UITestLogEntry corresponding to the given db_result.

        Parameters
        ----------
        db_result: the tuple returned by executing a query in our UI Test logs DB
        """
        self.id = db_result[0]
        self.test_suite = db_result[1]
        self.test_case = db_result[2]
        self.start_time = datetime.strptime(db_result[3], DB_DATETIME_FORMAT)
        self.end_time = datetime.strptime(db_result[4], DB_DATETIME_FORMAT)
        self.branch = db_result[5]
        self.machine = db_result[6]
        self.job = db_result[7]
        self.status = db_result[8]

    def __repr__(self) -> str:
        """Overrides the default __repr__ for dataclasses so that the output when this script is called during Jenkins
        runs is more readable.

        Returns
        -------
        A string representation of the database entry formatted like the following example:

        Test 'Selected Area - Max Elements' in 'suite_si_acquisition' Passed
            start time: 'Tue Jul 18 12:27:12 2023'
            end time: 'Tue Jul 18 12:28:33 2023'
            Velox binary: '\\veloxfileserver\binaries\54bbc91e'
            MPC: 'VELOX-25'
        """
        return (
            f"Test '{self.test_case}' in '{self.test_suite}' {self.status}"
            f"\n\tstart time: '{self.start_time.ctime()}'"
            f"\n\tend time: '{self.end_time.ctime()}'"
            f"\n\tVelox binary: '{self.branch}'"
            f"\n\tMPC: '{self.machine}'"
        )


class UITestLogDB:
    """Provides a Python interface for making queries to our UITestLog database."""

    def __init__(self) -> None:
        """Creates the connection and cursor to the database necessary for making queries."""
        self.__connection = sqlite3.connect(DB_PATH)
        self.__cursor = self.__connection.cursor()

    def get_last_n_tests(self, machine: str, num_results: int) -> List[UITestLogEntry]:
        """Gets the reults of the last test runs for a given machine. The number of results is equal to num_results.

        Parameters
        ----------
        machine: the MPC name to get the test results for
        num_results: how many of the last tests result should be fetched and returned

        Returns
        -------
        The results of the SQL query
        """
        raw_results = self.__cursor.execute(SELECT_LAST_N_TESTS_QUERY, (machine, num_results)).fetchall()
        return [UITestLogEntry(result) for result in raw_results]


# This module is intended to be run from the command line
#
# Right now, the only query supported is to get the last tests
# run by the MPC this module is being called from. The syntax to make this query is:
#   python ./framework/utils/sqllite.py get_last_n_tests 3
# The last argument can be changed to return more or less results.
if __name__ == "__main__":
    script_name = os.path.basename(os.path.realpath(__file__))
    if len(sys.argv) < 2:
        raise RuntimeError(f"{script_name} requires a command to be passed")

    valid_commands = ["get_last_n_tests"]
    command = sys.argv[1]
    if command not in valid_commands:
        raise RuntimeError(f"{script_name} expects a command in {valid_commands}. {command} is not a valid command.")

    if command == "get_last_n_tests":
        if len(sys.argv) != 3:
            raise RuntimeError("'get_last_n_tests' expects argument <number of results to return>")

        num_results = int(sys.argv[2])
        if num_results < 0:
            raise RuntimeError(
                "'get_last_n_tests' expects a positive integer argument for"
                f" <number of results to return>, not {num_results}"
            )

        hostname_result = subprocess.run(["hostname"], capture_output=True, text=True)
        if hostname_result.returncode != 0:
            raise RuntimeError(
                f"'hostname' returned exit code {hostname_result.returncode}."
                f"\n{hostname_result.stdout}{hostname_result.stderr}"
            )
        else:
            machine = hostname_result.stdout.strip().upper()

        if machine in DB_MACHINE_NAME_MAP:
            machine = DB_MACHINE_NAME_MAP[machine]
        elif machine not in DB_MACHINE_NAME_MAP.values():
            raise RuntimeError(
                f"'{machine}' is not a known MPC. Accepted values are"
                f"{list(DB_MACHINE_NAME_MAP.keys()) + list(DB_MACHINE_NAME_MAP.values())}"
            )

        results = UITestLogDB().get_last_n_tests(machine, num_results)
        for result in results:
            print(result)
