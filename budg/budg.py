#! /usr/bin/python3

########################################################################
# budg - my python script for budgeting my paychecks
#
# Copyright (C) 2022 Kyle Bouwman
#
# This file is part of budg.
#
# budg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# budg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with budg.  If not, see <https://www.gnu.org/licenses/gpl.html>.
########################################################################


# imports
import os
import sys
import math
from typing import Any
import tomli

# CONSTANTS
PLAN_DIRECTORY = os.path.join(os.path.expanduser("~"), "Documents", "budg")
USER_PLAN_FILENAME = "plan.toml"
DEFAULT_PLAN_FILENAME = "defaultplan.toml"


def usage_error() -> None:
    """Displays usage information"""
    print("Usage: budget XXX.XX")
    print("Invalid argument")
    exit(1)


def read_file(
    directory: str = PLAN_DIRECTORY,
    user_filename: str = USER_PLAN_FILENAME,
    default_filename: str = DEFAULT_PLAN_FILENAME,
) -> dict[str, Any]:
    """Parses data from plan file"""

    file_path = os.path.join(directory, user_filename)
    if not os.path.isfile(file_path):
        file_path = os.path.join(directory, default_filename)
        if not os.path.isfile(file_path):
            print(f"No config found. Please create one in '{directory}'.")
            exit(2)

    with open(file_path, "rb") as file:
        filedata = tomli.load(file)

    return filedata


def calculate_budget(plan: dict[str, Any], total: float) -> dict:
    """Calculates budget amounts based on plan for the given total"""

    budgit = {}

    def truncate_dollars(val: float) -> float:
        """Helper: Truncates decimals to the hundredths place"""

        if val == float("inf") or val == float("-inf"):
            return val
        factor = 100
        return math.floor(val * factor) / factor

    for category in plan:
        line_items = {}

        for item in plan[category]:
            value = float(plan[category][item]) * total
            value = truncate_dollars(value)
            line_items[item] = value

        budgit[category] = line_items

    return budgit


def print_budget(budget: dict) -> float:
    """Prints calculated budget to screen"""

    total = 0.0
    for category in budget:
        print(category)
        for item in budget[category]:
            name = item
            val = budget[category][item]

            if name != "total":
                total += val
            print(f"  {name}        ${val:.2f}")

    return total


def main(argv) -> None:
    """Driver function"""

    if len(argv) == 1:
        usage_error()

    amount = 0.0
    for val in argv[1:]:

        try:
            val = float(val)
        except ValueError:
            usage_error()

        amount += val

    plan = read_file()
    budget = calculate_budget(plan, amount)
    print_budget(budget)


if __name__ == "__main__":
    main(sys.argv)
    # main(["budg.py", "100"])  # XXX testing
