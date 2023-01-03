# Budg

A simple percentage-based budget calculator.

## Introduction

Say you have $236, and you want to split that 60/40. This script makes it easy!
Create a toml file like so:

```toml
categoryA = 60
categoryB = 40
```

and then run `budg $236`

```text
$ budg $236
=============================
categoryA          $   141.60
=============================
categoryB          $    94.40
=============================
```

And your toml file can be saved for future use. Much easier than breaking out
the calculator for every paycheck, and much more lightweight and flexible than
a spreadsheet.

- [Budg](#budg)
  - [Introduction](#introduction)
  - [Installation](#installation)
    - [Uninstallation](#uninstallation)
  - [Usage](#usage)
    - [Plans](#plans)
      - [Creating a plan](#creating-a-plan)
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

This script will copy the python file to `~/.local/bin/budg` and make it
executable.
Then, it will create the `budg` directory in your `Documents` folder and copy
the default plan file there.

### Uninstallation

You can also use `install.sh -u` to remove all traces of budg from your system.

Deletes the python file in `~/.local/bin` and the entire budg directory in
`~/Documents`.
**Make sure to save your plan toml files in a safe place if you want to keep
them!**

```text
$ ./install.sh -u
...
budg uninstalled
```

## Usage

Standard usage message:

```text
$ python budg.py -h
usage: budg.py [-h] [-p [name]] value [value ...]

Budget some dollars.

positional arguments:
  value                 the dollar amount you want to budget

options:
  -h, --help            show this help message and exit
  -p [name], --plan [name]
                        select the budget plan to use
```

`budg` takes one positional argument, but you can optionally pass more.

For example, to budget $100:

```text
$ budg 100
=============================
Necessities        $    50.00
=============================
Savings            $    20.00
=============================
Discretionary      $    30.00
=============================
```

You can use dollar signs, comma-separated groups, and multiple values.
Example (total: $2654.20):

```text
$ budg $123.45 1,443.21 1087.54
=============================
Necessities        $  1327.10
=============================
Savings            $   530.84
=============================
Discretionary      $   796.25
=============================
```

Here is the `plan.toml` file for the above:

```toml
Necessities = 50
Savings = 20
Discretionary = 30
```

### Plans

Budget plans are defined in toml files.
The file simply states a set of named categories and percentages as decimal
values between 0 and 1.
Budg divides your income into these weighted categories as defined by your plan.

Plan files are stored in `~/Documents/budg/`.
You can change your plan by modifying `~/Documents/budg/plan.toml`.
You can also tell budg to use a different plan file with the `-p`/`--plan`
option.

You can either use a path:

```text
$ budg -p /path/to/myplan.toml 100
...
```

Or the name of a file in `~/Documents/budg/`:

```text
$ ls ~/Documents/budg
plan.toml
otherplan.toml
$ budg -p otherplan 100
...
```

#### Creating a plan

Plans are toml files in `~/Documents/budg/` that outline your budget. Create
categories (and subcategories!) and assign each one a percentage.

Here is an example of a `plan.toml` file:

```toml
[Necessities]
rent = 30
gas_auto = 20

[Savings]
investments = 10
cash = 10

[Discretionary]
restaurants = 10
entertainment = 10
shopping = 10
```

Budg will use those percentages to divvy up your income and print the result.
Budgeting $100 with the plan above would give us this output:

```text
$ budg 100
=============================
Necessities        $    50.00
-----------------------------
> rent             $    30.00
> gas_auto         $    20.00
=============================
Savings            $    20.00
-----------------------------
> investments      $    10.00
> cash             $    10.00
=============================
Discretionary      $    30.00
-----------------------------
> restaurants      $    10.00
> entertainment    $    10.00
> shopping         $    10.00
=============================
```

**NOTE:**
The grand total is not verified or calculated in any way, _so you are
responsible for making sure you do not budget more than 100% of your income!_

A default budget plan based on [the 50/20/30 plan](#the-502030-plan) is created
when you install budg.

### The 50/20/30 Plan

The 50/20/30 plan is basic budget starting point that should work for most
people. It can be easily modified to fit your lifestyle, and I encourage you to
find a plan that fits your needs and priorities.

The model works by defining 3 major spending categories: Necessities, Savings,
and Discretionary.
Necessities are things you _must_ have: food, shelter, utilities, medical
expenses, transportation. If you need it to survive, or to earn more money,
then it is a necessity.
Savings is all about building wealth and working towards financial goals. This
category includes debt payments, investments, and general savings. This is the
most important category. _Pay yourself first!_
Discretionary is all the nice-to-haves. Things like restaurants, bars, and fun
activities.

Each category is given a weight (50%, 20%, and 30%, respectively).
You take your total after-tax income and divide it into the categories
according to weight, creating allowances for yourself. So, half of your income
will go toward necessities. Twenty percent should go towards savings, and
thirty percent towards discretionary.

![The 50/20/30 budget](https://www.thebalance.com/thmb/T7aTgYvTRfglPtW9C2TZFJSeSZQ=/950x0/filters:format(webp)/the-50-30-20-rule-of-thumb-453922-final-5b61ec23c9e77c007be919e1-5ecfc51b09864e289b0ee3fa0d52422f.png)

Image by (c) The Balance 2019.
Their article on the 50/20/30 budget can be found [here](https://www.thebalance.com/the-50-30-20-rule-of-thumb-453922).
You can also read more about the 50/20/30 budget [on Investopedia.](https://www.investopedia.com/ask/answers/022916/what-502030-budget-rule.asp)

I hope this quick little guide helped you get familiar with the 50/20/30 budget
and inspired ideas that you can implement in your own plan.

## License Notice

Copyright (C) 2020-2023 Kyle Bouwman

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
