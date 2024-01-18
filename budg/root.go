// budg
//
// Budgeting income the easy way
//
// by Kyle Bouwman
//
// Copyright (C) 2022-2024 Kyle Bouwman
//
// This file is part of budg.
//
// budg is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// budg is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with budg.  If not, see <https://www.gnu.org/licenses/gpl.html>.

// Tools for percentage-based income budgeting.
package budg

import (
	"fmt"
	"os"

	"strconv"

	"github.com/BurntSushi/toml"
	"github.com/spf13/cobra"
)

/*
Representation of a plan.
The outer and inner string keys are group name and item name, respectively.
The float value pointed to by the keys is a percentage amount (0-100) that
represents how much of the total budget belongs to that item.
*/
type BudgPlan map[string]map[string]float64

/*
Calculates the budget totals for each item and builds a string table
for output to the screen.
*/
func (plan BudgPlan) CalculateTable(amount float64) string {
	var ret string = ""
	for groupName, groupValue := range plan {
		ret += fmt.Sprintln(groupName)
		for itemName, itemValue := range groupValue {
			var itemRatio float64 = itemValue / 100
			var itemAmount float64 = amount * itemRatio
			var lineOut string = "  %-20s$%8.2f\n"
			ret += fmt.Sprintf(lineOut, itemName, itemAmount)
		}
	}
	return ret
}

var rootCmd = &cobra.Command{
	Use: "budg amount...",
	Example: "  budg 100\n" +
		"  budg '$123.45'\n" +
		"  budg 100 250 34.99 12.01",
	Short: "budg is a simple budget calculator",
	Long: "budg is a simple budget calculator\n" +
		"Enter a list of dollar amounts and it will divvy the total up\n" +
		"according to your plan.",
	Args: cobra.MinimumNArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		var plan BudgPlan
		toml.DecodeFile("plan.toml", &plan)

		var amount float64 = 0
		for _, arg := range args {
			if arg[0:1] == "$" {
				arg = arg[1:]
			}
			val, err := strconv.ParseFloat(arg, 64)
			if err != nil {
				fmt.Fprintln(os.Stderr, err)
				os.Exit(1)
			}
			amount += val
		}
		fmt.Print(plan.CalculateTable(amount))
	},
}

// Cobra function. Executes the command.
func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
