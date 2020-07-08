import budg
import configparser
import os.path


def getBudgitPlan():
    config = budg.readFile()
    plan = budg.parsePlan(config)
    return plan

plan = getBudgitPlan()

class TestBudgetCalc():

    def test_rounding_valid(self):
        amount = 1234.56
        result = budg.calcBudgit(plan, amount)
        result = budg.printBudgit(result)
        assert amount >= result

    def test_rounding_zero(self):
        amount = 0
        result = budg.calcBudgit(plan, amount)
        result = budg.printBudgit(result)
        assert amount >= result

    def test_rounding_one(self):
        amount = 1
        result = budg.calcBudgit(plan, amount)
        result = budg.printBudgit(result)
        assert amount >= result

    def test_rounding_inf(self):
        amount = float("inf")
        result = budg.calcBudgit(plan, amount)
        result = budg.printBudgit(result)
        assert amount >= result

    def test_rounding_scinote(self):
        amount = float("1e23")
        result = budg.calcBudgit(plan, amount)
        result = budg.printBudgit(result)
        assert amount >= result

    def test_rounding_neg(self):
        amount = -300.45
        result = budg.calcBudgit(plan, amount)
        result = budg.printBudgit(result)
        assert amount >= result
