#! /bin/bash

################################################################################
# Budg
# uninstall.sh
# by Kyle Bouwman
# subject to MIT License (see LICENSE)
#
# This script will remove Budg files from your system
################################################################################

BINFILE="$HOME"/bin/budg
CONFDIR="$HOME"/.config/budg
SCRIPTDIR="$HOME"/scripts/budg

rm -r "$BINFILE" "$CONFDIR" "$SCRIPTDIR"
