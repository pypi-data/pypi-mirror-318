# Copyright(c) 2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

import re
import test
from dataclasses import dataclass


@dataclass
class Tooltip:
    header: str
    message: str

    @classmethod
    def from_HTML(cls, html: str):
        """Parses the tooltip header and message from the tooltip HTML.

        Example HTML: <html><head/><body><p><span style=" font-weight:600;">Spectrum Imaging Area</span></p>
        <p>Draw the spectrum imaging area.</p></body></html>

        This HTML can be obtained by getting the toolTip property of appropriate Squish objects.

        Parameters
        ----------
        html: the raw HTML of the tooltip
        """
        tooltip_pattern = r"<span style=\" font-weight:600;\">(.+)</span></p><p>(.+)</p>"
        match = re.search(tooltip_pattern, html)
        if match:
            return cls(match.group(1), match.group(2))
        else:
            test.fail(f"tooltip HTML is not of the expected format: {html}")
