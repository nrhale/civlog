#!/usr/bin/env python3
from functions.log_gas import log_gas
from functions.report_economy import report_economy
from functions.utils import input_selection

print("### CIVLOG ###\n")

while True:
    print("# MAKE SELECTION")
    print("1. LOG GAS")
    print("2. REPORT FUEL ECONOMY")
    print("3. EXIT")
    selection = input_selection(3)

    if selection == 1:
        log_gas()
    elif selection == 2:
        report_economy()
    elif selection == 3:
        print("CLOSING CIVLOG.")
        break
