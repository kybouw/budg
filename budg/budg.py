#! /usr/bin/python3
"""
budg

Budgeting income the easy way

by Kyle Bouwman

Copyright (C) 2022-2023 Kyle Bouwman

This file is part of budg.

budg is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

budg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with budg.  If not, see <https://www.gnu.org/licenses/gpl.html>.
"""
import argparse
import math
import os
import re
import sys
from typing import Any

import tomli

PLAN_DIRECTORY = os.path.join(os.path.expanduser("~"), "Documents", "budg")


def get_path_to_plan(plan_name: str, plan_dir: str = PLAN_DIRECTORY) -> str:
    """Determines the path to the specified plan

    Parameters
    ----------
    plan_name: str
        A reference to a plan file somewhere. Can be a full path to the
        toml file or the name of a file inside plan_dir
    plan_dir: str, default PLAN_DIRECTORY
        The path to a directory of plan toml files to search through for
        plan_name.

    Returns
    -------
    str
        The full path to the plan toml file specified by plan_name
    """
    # helper
    def is_valid_file(s: str) -> bool:
        """Checks if s is a path to a valid plan toml file"""
        return os.path.isfile(s) and s.lower().endswith(".toml")

    # if plan_name is a valid plan file, return that path
    if is_valid_file(plan_name):
        return plan_name

    # helper
    def normalize(s: str) -> str:
        """Normalizes toml file names for comparison"""
        return s.lower().replace(".toml", "")

    # if plan_name is a valid name of a plan file in plan_dir,
    #   return the path to that file
    for item in os.scandir(plan_dir):
        if not is_valid_file(item.path):
            continue
        if normalize(item.name) == normalize(plan_name):
            return item.path

    # plan_name did not match
    print(f"Could not find file specified by '{plan_name}'")
    raise FileNotFoundError()


def make_budg_table(plan: dict[str, Any], budg_total: float) -> str:
    """Creates output text using calculated budget amounts based on plan
    for the given total

    Parameters
    ----------
    plan: dict[str, Any]
        A plan object
    budg_total: float
        The total amount to budget

    Returns
    -------
    str
        Formatted string with calculated budget values
    """
    # plans follow a major/minor format
    # There is major category that labels groups of budget categories,
    #   and a minor category that labels individual budget categories
    s = "=============================\n"
    for major in plan:
        # if major has no minor categories
        major_type: type = type(plan[major])
        if major_type is float or major_type is int:
            major_ratio = float(plan[major] / 100)
            major_amount = budg_total * major_ratio
            trunc_major_amount = math.floor(major_amount * 100) / 100
            formatted_amount = f"{trunc_major_amount:.2f}"
            s += f"{major:19}${formatted_amount:>9}\n"

        # if major is group of minor categories
        elif major_type is dict:
            major_sum_amount: float = 0
            # add placeholder for total at the end
            s += "00000000000000000000000000000\n"
            s += "-----------------------------\n"
            for category in plan[major]:
                # for backwards compatibility, skip "total" minor
                if str.lower(category) == "total":
                    continue
                # calculate the value of this category
                ratio = plan[major][category] / 100
                value = budg_total * ratio
                # truncate
                trunc_factor = 100
                trunc_value = math.floor(value * trunc_factor) / trunc_factor
                major_sum_amount += trunc_value
                # add to string
                value_formatted = f"{trunc_value:.2f}"
                s += f"> {category:17}${value_formatted:>9}\n"
            major_sum_formatted = f"{major_sum_amount:.2f}"
            # swap out placeholder for total major amount
            s = str.replace(
                s,
                "00000000000000000000000000000",
                f"{major:19}${major_sum_formatted:>9}",
            )
        s += "=============================\n"
    return s


def get_dollar_value(val_str: str) -> float:
    """Converts input to a float if it can be interpreted as a
    valid dollar amount. Returns 0 if input does not follow
    rules defined below.

    - Strings must not contain alphabet characters:
        123.45 or 123
        - 5e2 is not acceptable. Must be 500.
    - Strings may start with a dollar sign (USD only):
        $123.45 or $123
    - Strings may separate thousands groups with commas:
        123,456.78 or 1,200
        - comma groups must be groups of threes. No 1234,567 or 123,45
    - Values less than a dollar must start with a 0 before the decimal:
        0.32
    - Strings may only contain up to two decimal places:
        123.45
        - 5.5 is acceptable but will be interpreted as 5.50, not 5.05

    Parameters
    ----------
    val_str: str
        A string that represents a dollar amount

    Returns
    -------
    float
        A dollar amount as a float. Zero if string value does not follow
        format defined above.
    """
    # regex for recognizing dollar amount patterns as defined above
    dollar_amount_pattern = re.compile(
        pattern=r"^\$?(((\d{1,3}(,\d{3})*)|(\d+))(\.\d{0,2})?)$",
    )
    val_float: float = 0

    if re.fullmatch(dollar_amount_pattern, val_str) is not None:
        # string matches rules
        # remove $ and , and cast float
        no_commas = str.replace(val_str, ",", "")
        no_dollarsigns = str.replace(no_commas, "$", "")
        val_float = float(no_dollarsigns)
    else:
        # string does not match rules
        print(f"Could not interpret value: {val_str}")
        print("Try using a value in the form XXX.XX")
        if str.startswith(val_str, "."):
            print(
                "Values less than 1 must start with a 0",
                "\n e.g., .32 -> 0.32",
            )
        print()

    return val_float


def main(argv: list[str] = sys.argv) -> None:
    """Driver function.
    Handles high level program setup and user interfacing.

    Parameters
    ----------
    argv: list[str], default sys.argv
        A list of string arguments resembling that which would be
        returned by `sys.argv`.
        The list must be in the form of
        `["budg.py", {("-p", "plan_name",)|"-h"}, "float"]`
        where the part in `{}` is optional.
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
        plan_file_data = tomli.load(file)

    amount = 0.0
    for val in args.values:
        amount += get_dollar_value(val)

    budg_output = make_budg_table(plan_file_data, amount)
    print(budg_output)


if __name__ == "__main__":

    # XXX testing
    # main(["budg.py", "--plan", "test/test.toml", "100"])

    main()
