#! /usr/bin/python3

################################################################################
# budget.py
# by Kyle Bouwman
# subject to MIT License (see LICENSE)
#
# This is a script that helps me figure out how to budget my paychecks.
################################################################################

# imports
import configparser
import os.path
import os
import sys

# function that handles input errors
def usage_error():
    print('Usage: budget XXX.XX')
    print('Invalid argument')
    exit(1)
    
# verify args
if len(sys.argv) > 2:
    usage_error()

# The console object
class BudgConsole(object):

    # a dictionary for various possible commands the user could enter
    _commandBook = {
        "exit" : "exit",
        "quit" : "exit",
        "x" : "exit",
        "q" : "exit",
        "ex" : "exit",
        "paycheck" : "pc",
        "pc" : "pc",
        "check" : "pc",
        "income" : "pc",
    }

    # Constructor
    def __init__(self, config):

        # set the config
        print("Loading config file...")
        self.configfile = config
        self.cfgparser = configparser.ConfigParser()
        self.cfgparser.read(self.configfile)

        # clear the screen and welcome the user
        self.clearScreen()
        print('Welcome to the Budg Console\n\n')

        # start the console session
        self.runSession()

    # method that runs the session
    def runSession(self):
        # session loop
        sessionIsActive = True
        while sessionIsActive:
            # get user input
            cmd = input("budg> ")
            # read input
            sessionIsActive = self.readInput(cmd)

    # clears the screen
    def clearScreen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    # interprets the input command
    # returns true if user does not enter exit command
    def readInput(self, cmd):

        # interprets input to list of args
        consolev = cmd.split()

        # interprets first arg
        firstarg = "bad arg"
        if consolev[0] in self._commandBook:
            firstarg = self._commandBook[consolev[0]]

        # perform arg action
        if firstarg == "exit":
            return False
        elif firstarg == "pc":
            self.paycheck(consolev[1:])
        else:
            print(firstarg)

        # default action for non-exit
        return True

    def paycheck(self, amounts):
        total = 0.0
        valid = True
        for check in amounts:
            try:
                total += float(check)
            except:
                print("Invalid input")
                valid = False
                break

        if valid == True and total > 0:
            self.printBudget(total)

    def printBudget(self, check):
        for section in self.cfgparser.sections():
            print(section)
            for category in self.cfgparser[section]:
                val = float(self.cfgparser[section][category]) * check / 102
                txt = "  {}        ${:.2f}"
                print(txt.format(category, val))



# create vars
HOME = os.path.expanduser('~')
USERCONFIG = os.path.join(HOME, '.config/budg/budget.ini')
DEFCONFIG = os.path.join(HOME, '.config/budg/defaultbudget.ini')
CONFIG = None

# check for user config, try default config, exit in shame
if os.path.isfile(USERCONFIG):
    CONFIG = USERCONFIG
elif os.path.isfile(DEFCONFIG):
    CONFIG = DEFCONFIG
else:
    print("Config not found")
    exit(2)

# see if user wants interactive mode
if len(sys.argv) == 1:
    console = BudgConsole(CONFIG)
    exit(0)

# make sure that arg is a float
try:
    AMOUNT = float(sys.argv[1])
except:
    usage_error()

# parse config
config = configparser.ConfigParser()
config.read(CONFIG)

# go through categories in config
for section in config.sections():
    print(section)
    for category in config[section]:
        # calculate and show budget for category
        val = float(config[section][category]) * AMOUNT / 102
        txt = "  {}        ${:.2f}"
        print(txt.format(category, val))
