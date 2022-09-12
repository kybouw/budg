# Budg

Congratulations on taking hold of your financial freedom! The first step to building wealth is having a budgeting system that works _for_ you, so that you can focus on the important things in life.

This tool is meant to make budgets simpler by removing the need for spreadsheets and calculators. You simply outline your budget and whenever you get paid, just run the command and _voila!_ You have a guide that tells you exactly where your money needs to go! There are no servers or clouds involved, so you can rest easy knowing that your financial data is not being shared with anyone except yourself.

## Contents

- [Budg](#budg)
- [Contents](#contents)
- [Installation](#installation)
  - [Uninstallation](#uninstallation)
- [Usage](#usage)
  - [Plans](#plans)
    - [~/.config/budg/plan.ini](#configbudgplanini)
    - [~/.config/budg/defaultplan.ini](#configbudgdefaultplanini)
  - [Budgits](#budgits)
- [The 50/20/30 Plan](#the-502030-plan)
  - [Necessities - 50%](#necessities---50)
  - [Savings - 20%](#savings---20)
  - [Discretionary - 30%](#discretionary---30)
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

### Uninstallation

You can also use `install.sh -u` to remove all traces of budg from your system.

Deletes the python file in `~/.local/bin` and the entire budg directory in `~/.config`.
**Make sure to copy your `plan.ini` file somewhere else if you want to save it!**

```text
$ ./install.sh -u
...
budg uninstalled
```

## Usage

Once [installed](#installation), you can run your income through budg right away using the `budg <amount>` command. For example, to use the default budg plan to budget $123.00 in income:

```text
$ budg 123
Necessities
  total        $61.50
Savings
  total        $24.60
Discretionary
  total        $36.90
```

Using budg is easy, but there are a few things you need to know in order to make full use of budg.

Budg uses _plans_ to divide your income into categories. A [_plan_](#plans) is a set of rules that outlines your budget. Budg divides your income into weighted categories as defined by your plan. The result of this division is called a [_budgit_](#budgits).

You can change your plan by modifying `~/.config/budg/plan.ini`.

### Plans

Plans are documents that outline your budget. They tell budg how you want your money to be spent. These documents are stored in `~/.config/budg/`. The installer (`make install`) will create a default plan file for you.

#### ~/.config/budg/defaultplan.ini

This file is in the budg repository. The installation script copies this file to `~/.config/budg/defaultplan.ini`. It is a general implementation of [the 50/20/30 plan](#the-502030-plan).

#### ~/.config/budg/plan.ini

`~/.config/budg/plan.ini` is an outline of your budget. It contains all of the information needed to figure out where your money belongs. Plans are the key to budgeting; deciding where your money belongs before you spend it is what brings you financial security and peace of mind.

Plans are `ini` files and are stored inside your home directory (inside the path `~/.config/budg/`). : `defaultplan.ini` and `plan.ini`.

### Budgits

You can easily execute the program from your command line. Simply type `budg` followed by your paycheck value(s).
For example, show your budgit for a $123.45 paycheck like so:

```text
budg 123.45
```

Budg will then show you the amount of money that belongs in each item of your plan.

```text
$ budg 123.45
Necessities
  total        $61.72
Savings
  total        $24.69
Discretionary
  total        $37.03
```

You can also input multiple paychecks at once:

```text
$ budg 123.45 543.21 987.54
Necessities
  total        $827.10
Savings
  total        $330.84
Discretionary
  total        $496.26
```

## The 50/20/30 Plan

To get started with budg, a default budgit plan is provided: the 50/20/30 plan, a simple budget system popularized by U.S. Senator Elizabeth Warren. This model can easily be modified to fit the your needs, which is why Budg uses it as a starting point for building budgit plans.

The model works by defining 3 major spending categories: necessities, savings, and discretionary. Each category is given a weight (50%, 20%, and 30%, respectively). You take your total after-tax income and divide it into the categories according to weight, creating allowances for yourself. Once all of your allowances are calculated, you will know how every dollar you earned is going to work for you.

You are able to create your own budgit plans from the default plan. You can add or remove categories, change the weights of categories, and add subcategories to more precisely manage your income.

This guide will help you get familiar with the 50/20/30 budget and hopefully inspire ideas that you can implement in your own budgit plan.

![The 50/20/30 budget](https://www.thebalance.com/thmb/T7aTgYvTRfglPtW9C2TZFJSeSZQ=/950x0/filters:format(webp)/the-50-30-20-rule-of-thumb-453922-final-5b61ec23c9e77c007be919e1-5ecfc51b09864e289b0ee3fa0d52422f.png)Image by (c) The Balance 2019. Their article on the 50/20/30 budget can be found [here](https://www.thebalance.com/the-50-30-20-rule-of-thumb-453922).

### Necessities - 50%

Fifty percent of your after-tax income is meant for necessities. This includes anything that you cannot live without or anything you _must_ pay. Usually, this means things like rent, groceries, transportation, debt payments, insurance, and maybe your phone bill. Of course, you decide what belongs here, but make sure it only includes things that you **_need_**. Necessities is strictly the _must-have_ category and is typically the "boring" part of spending.

Once you know how much you can spend on necessities, try to keep your spending under that amount. If you find that you are spending too much on necessities, consider ways to save. Maybe refinancing your mortgages or loans, finding a cheaper place to live, switching to more affordable insurance, etc. If you are spending significantly less than your allowance, then perhaps you could allocate some of that excess to your savings allowance.

Upgrades to necessities often belong in the discretionary category. For example, the cost of the "premium" unlimited data phone plan over the most basic phone plan is a discretionary expense because you might _need_ a phone plan and not _need_ unlimited data. However, if your job requires you to stay on-call and online at all times, a premium phone plan could be considered a necessity. This category is all about _your_ needs!

### Savings - 20%

This is the most important part of any budget. At least twenty percent of your after-tax income is put into savings immediately after your paycheck hits your bank account. It's called **_paying yourself first_** (a.k.a **PYF**), and it is the key to financial security.

Now, "saving" does not necessarily mean just putting money into a savings account. No, this category includes all of your long-term savings goals: retirement accounts, savings accounts, investments, emergency funds, etc.

If you do not have one already, consider creating an emergency fund. An emergency fund is a savings account that will allow you to withdraw money when you need it, in case of emergencies that cause you to lose your income. You should have at least three months worth of your current income saved away in an emergency fund. Once your emergency fund is adequate, then you can pay more attention to your long term savings like retirement and investments.

This is the category that builds your financial future and gives you the security and peace of mind that you deserve. The whole point of budgeting is to save money. Be very hesitant to move money out of this category unless it is an absolute emergency.

### Discretionary - 30%

This is the "fun" category. It includes all of the things that you **_want_**, but maybe do not need. It includes restaurants, alcohol and recreation, movies and concerts, travel, spiffy new clothes, or the latest smartphone. This category is not just stand-alone expenses, but also any upgrades to the Necessities category that you want. Say, a nicer car or a faster internet service plan. These are the things that are completely _optional_, things you can get by without. However, just because you do not need these expenses does not mean you should ignore this category. This is the part of your budget that pays for the things that make life more fun and enjoyable. Putting money towards the things you want (and knowing that you are not hurting the bank by doing so) is the most rewarding part of keeping a budget.

[Read more about the 50/20/30 budget on Investopedia.](https://www.investopedia.com/ask/answers/022916/what-502030-budget-rule.asp)

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
