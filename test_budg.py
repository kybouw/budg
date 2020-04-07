import budg
import configparser
import os.path


def getBudget():
    config = configparser.ConfigParser()
    path = os.path.expanduser('~')
    path = os.path.join(path, '.config/budg/defaultbudget.ini')
    config.read(path)
    return config

budget = getBudget()

class TestBudgetCalc():

    def test_rounding_valid(self):
        amount = 1234.56
        result = budg.budget(amount, budget)
        assert amount >= result

    def test_rounding_zero(self):
        amount = 0
        result = budg.budget(amount, budget)
        assert amount >= result

    def test_rounding_one(self):
        amount = 1
        result = budg.budget(amount, budget)
        assert amount >= result

    def test_rounding_inf(self):
        amount = float("inf")
        result = budg.budget(amount, budget)
        assert amount >= result

    def test_rounding_scinote(self):
        amount = float("1e23")
        result = budg.budget(amount, budget)
        assert amount >= result

    def test_rounding_neg(self):
        amount = -300.45
        result = budg.budget(amount, budget)
        assert amount >= result
