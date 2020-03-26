#! /usr/bin/python3

################################################################################
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
################################################################################

# imports
import configparser
import os.path
import sys

# function that handles input errors
def usage_error():
    print('Usage: budget XXX.XX')
    print('Invalid argument')
    exit(1)
    
# handles program execution and input
def main(argc, argv):

    if(argc == 1):
        #TODO init interactive mode
        usage_error()

    else:
        # multiple values: budget their sum
        # amount = sum(float(val) for val in argv[1:])
        amount = 0.0
        for val in argv[1:]:

            # make sure that the arg is a decimal value
            try:
                val = float(val)
            except ValueError:
                usage_error()
            
            amount += val

        budget(amount)

# splits a dollar amount into a budget
def budget(amount):

    budget = parseBudget()

    for section in budget.sections():

        print(section)
        for item in budget[section]:

            # (percentage% * $amount) / 100 = $
            val = float(budget[section][item]) * amount / 100

            #TODO design/test rounding solution
            #XXX round to tenth of a penny, truncate to whole penny
            val = f"${val:.3f}"[:-1]

            #TODO look into f-string formatting: justify/width + decimal
            print(f"  {item}        {val}")

# look in the default budget location and parse a budget ini file there
def parseBudget():

    # create vars
    userhome = os.path.expanduser('~')
    userconfig = os.path.join(userhome, '.config/budg/budget.ini')
    defaultconfig = os.path.join(userhome, '.config/budg/defaultbudget.ini')

    parsedbudget = configparser.ConfigParser()

    # if config file already exists
    if os.path.isfile(userconfig):
        parsedbudget.read(userconfig)
        
    # if config file does not exist
    else:
        # use default budget, if present
        if os.path.isfile(defaultconfig):
            parsedbudget.read(defaultconfig)
        else:
            print("No config is found. Please create one in ~/.config/budg/")
            exit(2)

    return parsedbudget

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)