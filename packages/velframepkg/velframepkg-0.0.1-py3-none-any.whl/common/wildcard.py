# Copyright(c) 2022 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import re


class WildCard:
    def __init__(self, wild_card: str):
        self.pattern = re.compile(self._create_regex_str(wild_card))

    def search(self, item):
        return self.pattern.search(item)

    @staticmethod
    def _create_regex_str(wild_card: str):
        wild_card = wild_card.replace(".", r"\.").replace("?", ".").replace("*", ".*")
        # add line end and start
        return "^" + wild_card + "$"
