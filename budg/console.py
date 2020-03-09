#! /usr/bin/python3

###############################################################################
# console.py
# Budg
# by Kyle Bouwman
# subject to MIT License (see LICENSE)
#
# This is the module for the program's console
###############################################################################

import os


# The console object
class BudgConsole(object):

    # a dictionary for various possible commands the user could enter
    _commandBook = {
        "exit": "exit",
        "quit": "exit",
        "x": "exit",
        "q": "exit",
        "ex": "exit",
        "paycheck": "pc",
        "pc": "pc",
        "check": "pc",
        "income": "pc",
    }

    # Constructor
    # needs a budget object
    def __init__(self, budget):

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

        # Windows
        if os.name == 'nt':
            os.system('cls')

        # Mac or Linux
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

    # budget a paycheck
    def paycheck(self, amounts):

        # add up the total
        total = 0.0

        # check for valid inputs
        valid = True

        # loop through input amounts
        for check in amounts:

            try:
                # add to total
                total += float(check)

            except ValueError:

                # does not work if amount is not a decimal value
                print("Invalid input")
                valid = False
                break

        # print the budget if valid inputs
        if valid and total > 0:
            self.printBudget(total)

    # figure out how much money goes in each category, then print it
    def printBudget(self, check):

        # section by section...
        for section in self.cfgparser.sections():
            print(section)

            # calculate amount for each category
            for category in self.cfgparser[section]:

                val = float(self.cfgparser[section][category]) * check / 102

                # format and print
                txt = "  {}        ${:.2f}"
                print(txt.format(category, val))
