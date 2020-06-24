# budg

Congratulations on taking hold of your financial freedom! The first step to building wealth is having a budgeting system that works _for_ you, so that you can focus on the important things in life.

This tool is meant to make budgets simpler by removing the need for spreadsheets and calculators. You simply outline your budget and whenever you get paid, just run the command and _voila!_ You have a guide that tells you exactly where your money needs to go! There are no servers or clouds involved, so you can rest easy knowing that your financial data is not being shared with anyone except yourself.

## Contents

- [budg](#budg)
- [Contents](#contents)
- [Usage](#usage)
  - [plans](#plans)
  - [budgits](#budgits)
- [Installation](#installation)
- [Uninstallation](#uninstallation)
- [The 50/20/30 Plan](#the-502030-plan)
  - [Necessities - 50%](#necessities---50)
  - [Savings - 20%](#savings---20)
  - [Discretionary - 30%](#discretionary---30)
- [License Notice](#license-notice)

## Usage

Once you have [installed](#installation) budg, you will have a _plan_ file located inside of a config folder in your home directory (`~/.config/budg`). You can then use the `budg` command to calculate a _budgit_ that tells you where your money needs to go.

Here is an overview of how to use the tool:

1. Create a plan.
This is your outline for how to spend your money. One is included during installation, but you should keep on reading to find out how to make your own.
2. Evaluate your budgit using your income.
The `budg` command will take your income amount and divvy it up according to your plan. This new table including your dollar amounts is called a _budgit_.

### plans

A _plan_ is an outline of your budget. It contains all of the information needed to figure out where your money belongs. Plans are the key to budgeting; deciding where your money belongs before you spend it is what brings you financial security and peace of mind.

### budgits

You can easily execute the program from your command line. Simply type `budg` followed by your paycheck value(s).
For example, show your budgit for a $123.45 paycheck like so:

```text
budg 123.45
```

budg will then show you the amount of money that belongs in each item of your plan.

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

## Installation

budg can be installed using the bash script included in the repo.

1. Download the repo
2. cd into the repo
3. run `install.sh`

```text
$ git clone https://github.com/kybouw/budg.git
Cloning into 'budg'...
$ cd budg
$ ./install.sh
Starting install...
Install complete.
```

There is a little bit more output than shown here, but once you see the `Install complete.` message, you are ready to use budg!

## Uninstallation

There is also an uninstallation script included with the repo. You can run it the same way as the install script. However, it does not require any of the other files in the repo, so you can run it without the repo.

**Note:** the uninstall script will remove all budgit plans you have on your system. If you plan on reinstalling in the future, or if you just want to save the outline of your current budget, make sure to create a backup. Your plan is located in `~/.config/budg/`.

### Method 1 (**_recommended_**): the repo is already on your system

If you already have the repo from which you installed with on your system, then just use the uninstall script that was included with it. This is the recommended method for removing budg. Updated versions of the uninstall script may not be compatible with the version of budg that you have installed, so downloaded an updated uninstall script may not completely remove budg from your system.

1. Just run `uninstall.sh`

```text
$ ./path/to/repo/uninstall.sh
Uninstalling budg...
Uninstall completed.
```

Once you see `Uninstall completed.`, budg is removed from your system completely.

### Method 2: downloading the uninstaller

If you no longer have the repo installed, you can download the uninstaller standalone.

1. Download the script
2. Make it executable
3. Run the script

```text
$ curl https://raw.githubusercontent.com/kybouw/budg/master/uninstall.sh > uninstall.sh
$ chmod u+x uninstall.sh
$ ./uninstall.sh
Uninstalling budg...
Uninstall completed.
```

Once you see `Uninstall completed.`, budg is removed from your system completely.

## The 50/20/30 Plan

To get you started, a default plan is provided for you. It acts according to the 50/20/30 budget model, a simple budget system popularized by U.S. Senator Elizabeth Warren. This is the budget model that budg is built around. It works by taking your total income and dividing it into groups based on a percentage, creating a sort of "allowance" for yourself. Once you have that allowance calculated (which budg does for you), you are better equipped to make responsible spending decisions.

Here is how it works: you start by calculating your after-tax income. For the most part, this is just the value of your paycheck. Then, you divide that paycheck into three groups of unequal weight.

![The 50/20/30 budget](https://www.thebalance.com/thmb/T7aTgYvTRfglPtW9C2TZFJSeSZQ=/950x0/filters:format(webp)/the-50-30-20-rule-of-thumb-453922-final-5b61ec23c9e77c007be919e1-5ecfc51b09864e289b0ee3fa0d52422f.png)Image by (c) The Balance 2019. Their article on the 50/20/30 budget can be found [here](https://www.thebalance.com/the-50-30-20-rule-of-thumb-453922).

### Necessities - 50%

Fifty percent of that after-tax income is meant for necessities. This includes anything that you cannot live without. Usually, this means things like rent, groceries, transportation, debt payments, insurance, and maybe your phone bill. Of course, you decide what belongs here, but make sure it only includes things that you **_need_**. This is strictly the *must-have* category and is typically the "boring" part of spending.

Once you know how much you can spend, you should try to keep your spending under that. If you find that you are spending too much on the necessities, you should consider ways to save. Maybe refinancing your mortgage, finding a cheaper place to live, switching to more affordable insurance, etc. You could take money from other parts of your budget, but beware, you could be spending too much on something that you think you need but really belongs in another category. Upgrades to necessities belong in the discretionary category. For example, the cost of the "premium" unlimited data phone plan over the most basic phone plan is a discretionary expense because you can probably still live and work with a less expensive plan.

### Savings - 20%

This is what I consider to be the most important part of any budget. You should save at least twenty percent of your after-tax income immediately after your paycheck hits the bank. It's called *paying yourself first* (a.k.a "PYF"), and it is the key to making yourself more financially secure.

Now, "saving" does not necessarily mean just putting money into a savings account. No, this category includes all of your long-term savings goals: retirement accounts, savings accounts, investments, emergency funds, etc.

If you do not have one already, consider creating an emergency fund. An emergency fund is a savings account that will allow you to withdraw money whenever you need it, such as in the event of a loss of income. Most say that you should have at least three months worth of your current income saved away in an emergency fund. Once your emergency fund is adequate, then you can pay more attention to your retirement and investments.

This is the category that builds your financial future and gives you the security and peace of mind that you deserve. Be very hesitant to move money out of this category unless it is an absolute emergency.

### Discretionary - 30%

This is the "fun" category. It includes all of the things that you **_want_**, but maybe do not need. It includes restaurants, alcohol and recreation, movies and concerts, travel, spiffy new clothes, that unlimited data plan, speedy internet package, or the latest smartphone. This category is not just stand-alone expenses, but also any upgrades to the Necessities category that you want. Say, a nicer car or a new cell phone. These are the things that are completely *optional*, things you can get by without. However, just because they are optional, does not mean you should ignore this category, either. This is part of your budget that pays for the things that make life more fun and enjoyable.

[Read more about the 50/20/30 budget on Investopedia.](https://www.investopedia.com/ask/answers/022916/what-502030-budget-rule.asp)

## License Notice

Copyright (C) 2020 Kyle Bouwman

budg is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

budg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with budg.  If not, see <https://www.gnu.org/licenses/gpl.html>.
