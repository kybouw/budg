#! /usr/bin/python3
"""
budg

Budgeting income the easy way

by Kyle Bouwman

Copyright (C) 2022 Kyle Bouwman

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


def process_budget(plan: dict[str, Any], total: float) -> str:
    """Creates output text using calculated budget amounts based on plan
    for the given total

    Parameters
    ----------
    plan: dict[str, Any]
        A plan object
    total: float
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
    for group in plan:
        lcategories = [str.lower(x) for x in plan[group].keys()]
        if "total" in lcategories:
            raw_dvalue = total * (plan[group]["total"] / 100)
            trunc_dvalue = f"{(math.floor(raw_dvalue * 100) / 100):.2f}"
            dvalue = f"${trunc_dvalue:>9}"
        else:
            dvalue = ""
        s += f"{group:19}{dvalue}\n"
        s += "-----------------------------\n"
        for category in plan[group]:
            if str.lower(category) == "total":
                continue
            # calculate the value of this category
            ratio = plan[group][category] / 100
            value = total * ratio
            # truncate
            trunc_factor = 100
            value = math.floor(value * trunc_factor) / trunc_factor
            # print to screen
            value = f"{value:.2f}"
            s += f"> {category:17}${value:>9}\n"
            # s += "--------------------------\n"
        s += "=============================\n"
    return s


def main(argv: list[str] = sys.argv) -> None:
    """Driver function.
    Handles high level program setup and user interfacing.

    Parameters
    ----------
    argv: list[str], default sys.argv
        A list of string arguments resembling that which would be
        returned by 'sys.argv'.
        The list must be in the form of
        ["budg.py", {("-p", "plan_name",)|"-h"}, "float"]
        where the part in {} is optional.
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
        try:
            amount += float(val)
        except ValueError as e:
            print("Usage: budget XXX.XX")
            print("Invalid argument")
            raise ValueError("Could not understand number format") from e

    print(process_budget(plan_file_data, amount))


if __name__ == "__main__":

    # XXX testing
    # main(["budg.py", "--plan", "test/test.toml", "100"])

    main()
