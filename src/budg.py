#! /usr/bin/python3

###############################################################################
# budg - my python script for budgeting my paychecks
#
# Copyright (C) 2020 Kyle Bouwman
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
import os.path
import sys
import math


# constants
COMMANDS = {
    'exit': 'exit',
    'x': 'exit',
    'quit': 'exit',
    'q': 'exit',
    'pc': 'income',
    'income': 'income',
    'check': 'income'
}


# function that handles input errors
def usage_error():
    print('Usage: budget XXX.XX')
    print('Invalid argument')
    exit(1)


# handles program execution and input
def main(argc, argv):

    # console mode
    if argc == 1:
        # clear the screen
        clear_screen()

        # start the engine
        run_console_session()

    # single command mode
    else:
        run_single_session(argv[1:])


def run_single_session(argv):
    # multiple values: budget their sum
    # amount = sum(float(val) for val in argv[1:])
    amount = totalize(argv)
    plan = load_plan()
    budgit = calcBudgit(plan, amount)
    printBudgit(budgit)


# clears the terminal screen
def clear_screen():

    # windows
    if os.name == 'nt':
        os.system('cls')

    # mac and unix
    else:
        os.system('clear')


# controls loop for interactive mode
def run_console_session():

    # load plan
    plan = load_plan()

    # interaction loop
    running = True
    while running:

        # prompt
        argv = input('budg> ').split()

        # interpret commands
        if COMMANDS.get(argv[0]) == 'exit':
            # quit the console
            running = False

        elif COMMANDS.get(argv[0]) == 'income':
            # run budg on a set of income
            b = calcBudgit(plan, totalize(argv[1:]))
            printBudgit(b)

        else:
            # unknown command
            print("You said", argv)


# helper function for adding up income amounts
def totalize(values):

    # sum up the values
    amount = 0.0
    for val in values:

        # catch non-floats and throw an error
        try:
            amount += float(val)
        except ValueError:
            usage_error()

    return amount


# helper function for truncating decimals
def truncateDollars(val):
    if(val == float("inf") or val == float("-inf")):
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

            if(name != "total"):
                total += val
            # TODO look into f-string formatting: justify/width + decimal
            print(f"  {name}        ${val:.2f}")

    return total


# uses config parser to load the plan from disk
# file -> plan
def load_plan():

    # read ini into configparser
    # create vars
    userhome = os.path.expanduser('~')
    userconfig = os.path.join(userhome, '.config/budg/plan.ini')
    defaultconfig = os.path.join(userhome, '.config/budg/defaultplan.ini')

    filedata = configparser.ConfigParser()

    # if user config file exists, read it
    if os.path.isfile(userconfig):
        filedata.read(userconfig)

    # other wise check for default, and read that
    elif os.path.isfile(defaultconfig):
        filedata.read(defaultconfig)

    # no config exists
    else:
        print("No config is found. Please create one in ~/.config/budg/")
        exit(2)

    # decode configparser data into simple dictionary
    plan = {}
    for section in filedata.sections():
        line_items = {}
        for item in filedata[section]:
            line_items[item] = filedata[section][item]
        plan[section] = line_items

    return plan


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
