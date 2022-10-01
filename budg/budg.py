#! /usr/bin/python3

###############################################################################
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
###############################################################################


# imports
import configparser
import os
import sys
import math

# CONSTANTS
PLAN_DIRECTORY = path.join(path.expanduser("~"), "Documents", "budg")
USER_PLAN_FILENAME = "plan.ini"
DEFAULT_PLAN_FILENAME = "defaultplan.ini"


# function that handles input errors
def usage_error():
    print("Usage: budget XXX.XX")
    print("Invalid argument")
    exit(1)


# handles program execution and input
def main(argc, argv):

    if argc == 1:
        # TODO init interactive mode
        usage_error()

    # multiple values: budget their sum
    # amount = sum(float(val) for val in argv[1:])
    amount = 0.0
    for val in argv[1:]:

        try:
            val = float(val)
        except ValueError:
            usage_error()

        amount += val

    plan_cfg = readFile()
    plan = parsePlan(plan_cfg)
    budgit = calcBudgit(plan, amount)
    printBudgit(budgit)


# helper function for truncating decimals
def truncateDollars(val):
    if val == float("inf") or val == float("-inf"):
        return val
    factor = 100
    return math.floor(val * factor) / factor


# applies the budgit plan to the amount
# plan -> budgit
def calcBudgit(plan, total):

    budgit = {}

    for category in plan:
        line_items = {}

        for item in plan[category]:
            value = float(plan[category][item]) * total
            value = truncateDollars(value)
            line_items[item] = value

        budgit[category] = line_items

    return budgit


# prints the budgit object
# budgit -> output
def printBudgit(budgit):

    total = 0.0
    for category in budgit:
        print(category)
        for item in budgit[category]:
            name = item
            val = budgit[category][item]

            if name != "total":
                total += val
            # TODO look into f-string formatting: justify/width + decimal
            print(f"  {name}        ${val:.2f}")

    return total


def readFile(
    directory: os.PathLike = PLAN_DIRECTORY,
    user_filename: os.PathLike = USER_PLAN_FILENAME,
    default_filename: os.PathLike = DEFAULT_PLAN_FILENAME,
) -> configparser.ConfigParser:
    """Parses data from plan file"""

    file_path = os.path.join(directory, user_filename)
    if not os.path.isfile(file_path):
        file_path = os.path.join(os.path.split(file_path)[0], default_filename)
    if not os.path.isfile(file_path):
        print(f"No config found. Please create one in '{directory}'.")
        return None

    filedata = configparser.ConfigParser()
    filedata.read(file_path)
    return filedata


# turns file data from configparser to a budgit plan
# ConfigParser -> plan
def parsePlan(filedata):

    plan = {}
    for section in filedata.sections():
        line_items = {}
        for item in filedata[section]:
            line_items[item] = filedata[section][item]
        plan[section] = line_items

    return plan


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
