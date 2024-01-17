package budg

import (
	"fmt"
	"os"

	"strconv"

	"github.com/BurntSushi/toml"
	"github.com/spf13/cobra"
)

type BudgPlan map[string]map[string]float64

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
	Use:   "budg",
	Short: "budg is a simple budget calculator",
	Long:  "budg is a simple budget calculator",
	Run: func(cmd *cobra.Command, args []string) {
		var plan BudgPlan
		toml.DecodeFile("plan.toml", &plan)

		var amount float64 = 0
		for _, arg := range args {
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

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
