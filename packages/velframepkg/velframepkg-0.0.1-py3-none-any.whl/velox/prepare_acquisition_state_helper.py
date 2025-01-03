# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import squish
import test


def prepare_acquisition_state():
    from TemServer import instrument

    """Bring the simulator in a proper acquisition state."""
    # Timeout for the column to take into account command and being in a stable state
    column_timeout = 10000
    test.log("Prepare acquisition, check vacuum state")
    success = squish.waitFor(lambda: instrument.vacuum.is_ready(), column_timeout)
    if not success:
        test.fail("Vacuum is not ready")
    # Force opening column valves. This prevents a popup
    if not instrument.vacuum.valves_are_open():
        success = squish.waitFor(lambda: not instrument.vacuum.valves_are_not_allowed(), column_timeout)
        if not success:
            test.fail("Vacuum does not allow to open valves")

        test.log("Trying to open the column valves")
        instrument.vacuum.open_valves()
        # Settling time for slow systems (e.g. Titan)
        success = squish.waitFor(lambda: instrument.vacuum.valves_are_open(), column_timeout)
        if not success:
            test.fail("Could not open column valves")

        # After Holder insertion test, it can take some time to be able to open again the column valves
        test.log("Wait for vacuum is no more ready (not allowed state)")
        squish.waitFor(lambda: instrument.vacuum.valves_are_not_allowed(), column_timeout)
        test.log("Wait for vacuum is ready")
        success = squish.waitFor(lambda: not instrument.vacuum.valves_are_not_allowed(), column_timeout)
        if not success:
            test.fail("Column valves opening is not allowed")
        success = squish.waitFor(lambda: instrument.vacuum.is_ready(), column_timeout)
        if not success:
            test.fail("Vacuum is not ready after opening column valves")

    if not instrument.vacuum.valves_are_open():
        test.fail("Column valves can not be opened")
    else:
        test.log("Column valves are opened")
