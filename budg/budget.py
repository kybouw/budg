#! /usr/bin/python3

###############################################################################
# budget.py
# Budg
# by Kyle Bouwman
#
# Copyright (c) 2020 Kyle Bouwman
# subject to MIT License (see LICENSE)
#
# This module contains the budget object
###############################################################################

import configparser

class Budget(object):

    #attributes
    
    # constructor. initializes configparser and sets path to file
    def __init__(self, path):
        self.filepath = path
        self.parsedfile = configparser.ConfigParser()
        self.parsedfile.read(path)

    # changes the path to file
    def setPath(self, path):
        self.filepath = path

    # writes the budget to file
    def write(self):
        with open(self.filepath, 'w') as budgetfile:
            self.parsedfile.write(budgetfile)

    def funcname(self, parameter_list):
        pass