# Copyright(c) 2021-2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import os

from common import FileUtils
from utils.test_file_repo import create_directory_in_local_temp


class PerformanceUtils:
    def __init__(self):
        self.temp_dir = create_directory_in_local_temp("Performance")
        self.cur_csv_file = None
        self.cur_csv_file_name = None

    def get_unique_csv_file(self, name: str):
        self.cur_csv_file_name = FileUtils().get_unique_filename(f"{name}_", ".csv")
        self.cur_csv_file = os.path.join(self.temp_dir, self.cur_csv_file_name)
        return open(self.cur_csv_file, "wt")
