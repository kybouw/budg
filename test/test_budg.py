import configparser
import os.path

from budg import budg


def get_budget_plan():

    config = configparser.ConfigParser()
    def_plan_path = os.path.join(os.path.curdir, "testplan.ini")
    if os.path.isfile(def_plan_path):
        config.read(def_plan_path)

    plan = budg.parse_plan(config)
    return plan


plan = get_budget_plan()


class TestBudgetCalc:
    def test_rounding_valid(self):
        amount = 1234.56
        result = budg.calculate_budget(plan, amount)
        result = budg.print_budget(result)
        assert amount >= result

        # XXX this is just to show that rounding method
        # gets pretty close to the answer
        assert 1234.50 < result

    def test_rounding_zero(self):
        amount = 0
        result = budg.calculate_budget(plan, amount)
        result = budg.print_budget(result)
        assert amount == result

    def test_rounding_one(self):
        amount = 1
        result = budg.calculate_budget(plan, amount)
        result = budg.print_budget(result)
        assert amount == result

    def test_rounding_inf(self):
        amount = float("inf")
        result = budg.calculate_budget(plan, amount)
        result = budg.print_budget(result)

        # XXX this is kinda iffy too
        assert amount >= result

    def test_rounding_scinote(self):
        amount = float("1e23")
        result = budg.calculate_budget(plan, amount)
        result = budg.print_budget(result)
        assert amount == result

    def test_rounding_neg(self):
        amount = -300.45
        result = budg.calculate_budget(plan, amount)
        result = budg.print_budget(result)
        assert amount >= result
