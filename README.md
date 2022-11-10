# Budg

A simple percentage-based budget calculator.

- [Budg](#budg)
  - [Installation](#installation)
    - [Uninstallation](#uninstallation)
  - [Usage](#usage)
    - [Plans](#plans)
    - [The 50/20/30 Plan](#the-502030-plan)
  - [License Notice](#license-notice)

## Installation

Budg can be installed using the bash script `install.sh`.

1. Download the repo
2. cd into the repo
3. run `./install.sh`

```text
$ git clone https://github.com/kybouw/budg.git
Cloning into 'budg'
...
$ cd budg
$ ./install.sh
...
Install succeeded
```

This script will copy the python file to `~/.local/bin/budg` and make it executable.
Then, it will create the `budg` directory in your `Documents` folder and copy the default plan file there.

### Uninstallation

You can also use `install.sh -u` to remove all traces of budg from your system.

Deletes the python file in `~/.local/bin` and the entire budg directory in `~/Documents`.
**Make sure to save your `plan.toml` file in a safe place if you want to keep it!**

```text
$ ./install.sh -u
...
budg uninstalled
```

## Usage

Once [installed](#installation), you can run your income through budg right away using the `budg` command. For example, say you want to budget $100.00 in income:

```text
$ budg 100
Necessities
  total        $50.00
Savings
  total        $20.00
Discretionary
  total        $30.00
```

You can also input multiple incomes at once. Budg will sum them for you:

```text
$ budg 123.45 543.21 987.54
Necessities
  total        $827.10
Savings
  total        $330.84
Discretionary
  total        $496.26
```

Budg uses _plans_ to divide your income into categories.
A [_plan_](#plans) is simply a set of named categories and percentages that outline your budget.
Budg divides your income into these weighted categories as defined by your plan.

You can change your plan by modifying `~/Documents/budg/plan.toml`.

### Plans

Plans are toml files in `~/Documents/budg/` that outline your budget. Create categories (and subcategories!) and assign each one a percentage.

Budg will divide your income by those percentages into each category and print the result.

Here is an example of a `plan.toml` file:

```toml
[Necessities]
rent = 0.30
gas_auto = 0.20
total = 0.50

[Savings]
investments = 0.10
cash = 0.10
total = 0.20

[Discretionary]
restaurants = 0.10
entertainment = 0.10
shopping = 0.10
total = 0.30
```

Running budg with $100 would give us this output:

```text
$ budg 100
Necessities
  rent        $30.00
  gas_auto        $20.00
  total        $50.00
Savings
  investments        $10.00
  cash        $10.00
  total        $20.00
Discretionary
  restaurants        $10.00
  entertainment        $10.00
  shopping        $10.00
  total        $30.00
```

A default budget plan based on [the 50/20/30 plan](#the-502030-plan) is created when you install budg.

### The 50/20/30 Plan

The 50/20/30 plan is basic budget starting point that should work for most people. It can be easily modified to fit your lifestyle, and I encourage you to find a plan that fits your needs and priorities.

The model works by defining 3 major spending categories: Necessities, Savings, and Discretionary.
Necessities are things you _must_ have: food, shelter, utilities, medical expenses, transportation. If you need it to survive, or to earn more money, then it is a necessity.
Savings is all about building wealth and working towards financial goals. This category includes debt payments, investments, and general savings. This is the most important category. _Pay yourself first!_
Discretionary is all the nice-to-haves. Things like restaurants, bars, and fun activities.

Each category is given a weight (50%, 20%, and 30%, respectively).
You take your total after-tax income and divide it into the categories according to weight, creating allowances for yourself. So, half of your income will go toward necessities. Twenty percent should go towards savings, and thirty percent towards discretionary.

![The 50/20/30 budget](https://www.thebalance.com/thmb/T7aTgYvTRfglPtW9C2TZFJSeSZQ=/950x0/filters:format(webp)/the-50-30-20-rule-of-thumb-453922-final-5b61ec23c9e77c007be919e1-5ecfc51b09864e289b0ee3fa0d52422f.png)

Image by (c) The Balance 2019.
Their article on the 50/20/30 budget can be found [here](https://www.thebalance.com/the-50-30-20-rule-of-thumb-453922).
You can also read more about the 50/20/30 budget [on Investopedia.](https://www.investopedia.com/ask/answers/022916/what-502030-budget-rule.asp)

I hope this quick little guide helped you get familiar with the 50/20/30 budget and inspired ideas that you can implement in your own plan.

## License Notice

Copyright (C) 2020-2022 Kyle Bouwman

Budg is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Budg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with budg. If not, see <https://www.gnu.org/licenses/gpl.html>.
