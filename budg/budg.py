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


import argparse
import math
import os
import sys
from typing import Any

import tomli

PLAN_DIRECTORY = os.path.join(os.path.expanduser("~"), "Documents", "budg")
USER_PLAN_FILENAME = "plan.toml"
DEFAULT_PLAN_FILENAME = "defaultplan.toml"


def get_path_to_plan(input: str, plan_dir: str = PLAN_DIRECTORY) -> str:
    """Verifies path to plan file, or determines path based on name"""

    # if input is a valid plan file, return that path
    if os.path.isfile(input) and input.lower().endswith(".toml"):
        return input

    # quick helper
    def normalize(s: str) -> str:
        return s.lower().replace(".toml", "")

    # if input is a valid name of a plan file in plan dir,
    #   return the formulated path
    for item in os.scandir(plan_dir):
        if not (item.is_file() and item.name.lower().endswith(".toml")):
            continue
        if normalize(item.name) == normalize(input):
            return item.path

    # input did not match
    print(f"Could not find file specified by '{input}'")
    raise FileNotFoundError()


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


def main(argv: list[str] = sys.argv) -> None:
    """Driver function
    Handles high level program setup and user interfacing.
    """

    parser = argparse.ArgumentParser(description="Budget some dollars.")
    parser.add_argument(
        "values",
        metavar="value",
        type=str,
        nargs="+",
        help="the dollar amount you want to budget",
    )
    parser.add_argument(
        "-p",
        "--plan",
        metavar="name",
        type=str,
        nargs="?",
        help="select the budget plan to use",
        default="plan",
    )
    args = parser.parse_args(argv[1:])

    plan_path = get_path_to_plan(args.plan)
    with open(plan_path, "rb") as file:
        plan_obj = tomli.load(file)

    amount = 0.0
    for val in args.values:
        try:
            amount += float(val)
        except ValueError as e:
            print("Usage: budget XXX.XX")
            print("Invalid argument")
            raise ValueError("Could not understand number format") from e

    budget = calculate_budget(plan_obj, amount)
    print_budget(budget)


if __name__ == "__main__":

    # XXX testing
    # main(["budg.py", "100"])

    main()
