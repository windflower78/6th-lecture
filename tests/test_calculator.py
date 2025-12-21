"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_raises_invalid_input_when_a_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(1_000_001, 0)

    def test_add_raises_invalid_input_when_b_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(0, 1_000_001)
            
class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        calc = Calculator()
        assert calc.subtract(8, 3) == 5

    def test_subtract_raises_invalid_input_when_a_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(1_000_001, 0)

    def test_subtract_raises_invalid_input_when_b_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(0, -1_000_001)

class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        calc = Calculator()
        assert calc.multiply(6, 7) == 42

    def test_multiply_raises_invalid_input_when_a_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(1_000_001, 1)

    def test_multiply_raises_invalid_input_when_b_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(0, -1_000_001)

class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        calc = Calculator()
        assert calc.divide(9, 3) == 3

    def test_divide_by_zero_raises_value_error(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.divide(1, 0)

    def test_divide_raises_invalid_input_when_a_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(1_000_001, 1)

    def test_divide_raises_invalid_input_when_b_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(1, 1_000_001)