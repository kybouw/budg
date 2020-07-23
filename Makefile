

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

.PHONY: all install clean clean-bin

all:
	# You find a strange lantern. You hold it by your ear and shake it around 
	# to hear if anything is inside. You hear a faint voice whisper a
	fortune


install: src/budg.py src/defaultplan.ini
	# Creating directories...
	mkdir -p ~/.config/budg
	mkdir -p ~/bin
	# Copying program...
	cp src/budg.py ~/bin/budg
	chmod u+x ~/bin/budg
	# Copying config...
	cp src/defaultplan.ini ~/.config/budg/defaultplan.ini
	# Install Complete. (add ~/bin to PATH)


clean:
	# Removing budg...
	rm ~/bin/budg 
	rm -r ~/.config/budg
	# budg uninstalled


clean-bin: ~/bin/budg
	# removing budg...
	rm ~/bin/budg
	# budg removed