#! /bin/bash

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

echo "Uninstalling budg..."

BINFILE="$HOME"/bin/budg
CONFDIR="$HOME"/.config/budg

rm -r "$BINFILE" "$CONFDIR"

echo "Uninstall completed."
