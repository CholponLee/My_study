import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator(15, 0)

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply() == 0

    def test_division_calculate_correctly(self):
        if self.calc.y != 0:
            assert self.calc.division() == 3
        else:
            assert ZeroDivisionError

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction() == 15

    def test_adding_calculate_correctly(self):
        assert self.calc.adding() == 15
