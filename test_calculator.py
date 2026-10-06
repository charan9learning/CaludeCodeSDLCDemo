"""
Comprehensive pytest unit tests for the calculator.py application.

This test suite provides thorough coverage of all calculator functions including:
- Arithmetic operations (add, subtract, multiply, divide)
- Input validation (is_valid_number)
- Orchestration and error handling (perform_calculation)
- Edge cases: division by zero, negative numbers, floats, zero values
- Boundary conditions and special numeric values

Test Organization:
- TestValidation: Tests for is_valid_number() function
- TestArithmeticOperations: Tests for add, subtract, multiply, divide functions
- TestPerformCalculation: Tests for the orchestration function
- Parameterized tests for efficient coverage of multiple similar scenarios
"""

import pytest
from unittest.mock import patch, MagicMock
from calculator import (
    is_valid_number,
    add,
    subtract,
    multiply,
    divide,
    perform_calculation,
    get_first_number,
    get_second_number,
    get_operation,
    main,
)


class TestValidation:
    """Test suite for input validation with is_valid_number()."""

    # Happy path: valid numeric inputs
    def test_valid_integer_string(self):
        """Test that valid integer string is recognized as valid number."""
        assert is_valid_number("42") is True

    def test_valid_negative_integer_string(self):
        """Test that negative integer string is recognized as valid number."""
        assert is_valid_number("-42") is True

    def test_valid_float_string(self):
        """Test that valid float string is recognized as valid number."""
        assert is_valid_number("3.14") is True

    def test_valid_negative_float_string(self):
        """Test that negative float string is recognized as valid number."""
        assert is_valid_number("-3.14") is True

    def test_valid_zero_string(self):
        """Test that zero string is recognized as valid number."""
        assert is_valid_number("0") is True

    def test_valid_zero_float_string(self):
        """Test that zero as float is recognized as valid number."""
        assert is_valid_number("0.0") is True

    # Edge cases: boundary numeric values
    def test_valid_very_large_number_string(self):
        """Test that very large number string is recognized as valid."""
        assert is_valid_number("999999999999999999.99") is True

    def test_valid_very_small_number_string(self):
        """Test that very small (negative) number string is recognized as valid."""
        assert is_valid_number("-999999999999999999.99") is True

    def test_valid_scientific_notation(self):
        """Test that scientific notation is recognized as valid number."""
        assert is_valid_number("1e5") is True

    def test_valid_negative_scientific_notation(self):
        """Test that negative scientific notation is recognized as valid number."""
        assert is_valid_number("-1.5e-3") is True

    # Invalid inputs
    def test_invalid_empty_string(self):
        """Test that empty string is not recognized as valid number."""
        assert is_valid_number("") is False

    def test_invalid_text_string(self):
        """Test that text string is not recognized as valid number."""
        assert is_valid_number("abc") is False

    def test_invalid_special_characters(self):
        """Test that special characters are not recognized as valid number."""
        assert is_valid_number("@#$%") is False

    def test_invalid_text_with_numbers(self):
        """Test that mixed text and numbers are not recognized as valid number."""
        assert is_valid_number("12abc") is False

    def test_invalid_multiple_decimal_points(self):
        """Test that multiple decimal points are not recognized as valid number."""
        assert is_valid_number("1.2.3") is False

    def test_invalid_whitespace_only(self):
        """Test that whitespace-only string is not recognized as valid number."""
        assert is_valid_number("   ") is False

    def test_invalid_operator_string(self):
        """Test that operator symbols are not recognized as valid number."""
        assert is_valid_number("+") is False
        assert is_valid_number("-") is False
        assert is_valid_number("*") is False

    # Parameterized tests for comprehensive coverage
    @pytest.mark.parametrize("valid_input", [
        "0", "-0", "1", "-1", "42", "-42", "3.14", "-3.14",
        "0.5", "-0.5", "100", "1000000", "0.00001"
    ])
    def test_valid_numbers_parametrized(self, valid_input):
        """Parametrized test for various valid numeric strings."""
        assert is_valid_number(valid_input) is True

    @pytest.mark.parametrize("invalid_input", [
        "", "abc", "1.2.3", "hello42", "42.5.10", " ", "NaN", "infinity"
    ])
    def test_invalid_numbers_parametrized(self, invalid_input):
        """Parametrized test for various invalid numeric strings."""
        assert is_valid_number(invalid_input) is False


class TestArithmeticOperations:
    """Test suite for arithmetic operations: add, subtract, multiply, divide."""

    # Addition tests
    def test_add_positive_integers(self):
        """Test addition of two positive integers."""
        assert add(2, 3) == 5

    def test_add_negative_integers(self):
        """Test addition of two negative integers."""
        assert add(-2, -3) == -5

    def test_add_mixed_sign_integers(self):
        """Test addition of positive and negative integers."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2

    def test_add_zeros(self):
        """Test addition involving zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5

    def test_add_floats(self):
        """Test addition of floating point numbers."""
        assert add(1.5, 2.5) == 4.0
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_add_negative_floats(self):
        """Test addition of negative floating point numbers."""
        assert add(-1.5, -2.5) == -4.0

    def test_add_very_large_numbers(self):
        """Test addition of very large numbers."""
        assert add(1e10, 2e10) == 3e10

    # Subtraction tests
    def test_subtract_positive_integers(self):
        """Test subtraction of two positive integers."""
        assert subtract(5, 3) == 2

    def test_subtract_negative_integers(self):
        """Test subtraction of two negative integers."""
        assert subtract(-5, -3) == -2

    def test_subtract_mixed_sign_integers(self):
        """Test subtraction with mixed signs."""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8

    def test_subtract_zeros(self):
        """Test subtraction involving zero."""
        assert subtract(0, 0) == 0
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5

    def test_subtract_floats(self):
        """Test subtraction of floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0

    def test_subtract_results_in_negative(self):
        """Test subtraction resulting in negative number."""
        assert subtract(3, 5) == -2

    # Multiplication tests
    def test_multiply_positive_integers(self):
        """Test multiplication of two positive integers."""
        assert multiply(3, 4) == 12

    def test_multiply_negative_integers(self):
        """Test multiplication of two negative integers."""
        assert multiply(-3, -4) == 12

    def test_multiply_mixed_sign_integers(self):
        """Test multiplication with mixed signs."""
        assert multiply(3, -4) == -12
        assert multiply(-3, 4) == -12

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(0, 0) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0

    def test_multiply_by_one(self):
        """Test multiplication by one."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5

    def test_multiply_floats(self):
        """Test multiplication of floating point numbers."""
        assert multiply(2.5, 4.0) == 10.0

    def test_multiply_very_large_numbers(self):
        """Test multiplication of very large numbers."""
        assert multiply(1e5, 2e5) == 2e10

    # Division tests
    def test_divide_positive_integers(self):
        """Test division of two positive integers."""
        assert divide(6, 2) == 3.0

    def test_divide_negative_integers(self):
        """Test division of two negative integers."""
        assert divide(-6, -2) == 3.0

    def test_divide_mixed_sign_integers(self):
        """Test division with mixed signs."""
        assert divide(6, -2) == -3.0
        assert divide(-6, 2) == -3.0

    def test_divide_floats(self):
        """Test division of floating point numbers."""
        assert divide(5.0, 2.0) == pytest.approx(2.5)

    def test_divide_zero_numerator(self):
        """Test division with zero as numerator."""
        assert divide(0, 5) == 0.0

    def test_divide_by_zero_returns_none(self):
        """Test that division by zero returns None (codebase convention)."""
        assert divide(5, 0) is None
        assert divide(0, 0) is None
        assert divide(-5, 0) is None

    def test_divide_result_less_than_one(self):
        """Test division resulting in value less than one."""
        assert divide(1, 2) == pytest.approx(0.5)

    def test_divide_very_small_numbers(self):
        """Test division of very small numbers."""
        assert divide(0.001, 0.01) == pytest.approx(0.1)

    # Parameterized arithmetic tests
    @pytest.mark.parametrize("num1,num2,expected", [
        (1, 2, 3),
        (-1, -2, -3),
        (5, 0, 5),
        (0, 0, 0),
        (10, -5, 5),
    ])
    def test_add_parametrized(self, num1, num2, expected):
        """Parametrized test for add function."""
        assert add(num1, num2) == expected

    @pytest.mark.parametrize("num1,num2,expected", [
        (5, 3, 2),
        (-5, -3, -2),
        (5, 0, 5),
        (0, 0, 0),
        (3, 5, -2),
    ])
    def test_subtract_parametrized(self, num1, num2, expected):
        """Parametrized test for subtract function."""
        assert subtract(num1, num2) == expected

    @pytest.mark.parametrize("num1,num2,expected", [
        (3, 4, 12),
        (-3, -4, 12),
        (3, -4, -12),
        (0, 5, 0),
        (5, 0, 0),
    ])
    def test_multiply_parametrized(self, num1, num2, expected):
        """Parametrized test for multiply function."""
        assert multiply(num1, num2) == expected

    @pytest.mark.parametrize("num1,num2,expected", [
        (6, 2, 3.0),
        (-6, -2, 3.0),
        (6, -2, -3.0),
        (0, 5, 0.0),
    ])
    def test_divide_parametrized(self, num1, num2, expected):
        """Parametrized test for divide function with valid results."""
        assert divide(num1, num2) == expected

    @pytest.mark.parametrize("num1", [5, -5, 0, 0.5, -0.5])
    def test_divide_by_zero_parametrized(self, num1):
        """Parametrized test for division by zero returning None."""
        assert divide(num1, 0) is None


class TestPerformCalculation:
    """Test suite for perform_calculation orchestration function."""

    # Addition operation tests
    def test_perform_calculation_addition(self):
        """Test perform_calculation with addition operation."""
        assert perform_calculation(2, 3, '+') == 5

    def test_perform_calculation_addition_negative(self):
        """Test perform_calculation with addition of negative numbers."""
        assert perform_calculation(-2, -3, '+') == -5

    # Subtraction operation tests
    def test_perform_calculation_subtraction(self):
        """Test perform_calculation with subtraction operation."""
        assert perform_calculation(5, 3, '-') == 2

    def test_perform_calculation_subtraction_negative(self):
        """Test perform_calculation with subtraction of negative numbers."""
        assert perform_calculation(-5, -3, '-') == -2

    # Multiplication operation tests
    def test_perform_calculation_multiplication(self):
        """Test perform_calculation with multiplication operation."""
        assert perform_calculation(3, 4, '*') == 12

    def test_perform_calculation_multiplication_negative(self):
        """Test perform_calculation with multiplication of negative numbers."""
        assert perform_calculation(-3, -4, '*') == 12

    # Division operation tests
    def test_perform_calculation_division(self):
        """Test perform_calculation with division operation."""
        assert perform_calculation(6, 2, '/') == 3.0

    def test_perform_calculation_division_negative(self):
        """Test perform_calculation with division of negative numbers."""
        assert perform_calculation(-6, -2, '/') == 3.0

    # Division by zero handling
    def test_perform_calculation_division_by_zero_returns_none(self):
        """Test perform_calculation division by zero returns None."""
        assert perform_calculation(5, 0, '/') is None

    def test_perform_calculation_division_by_zero_prints_error(self, capsys):
        """Test that division by zero prints error message."""
        perform_calculation(5, 0, '/')
        captured = capsys.readouterr()
        assert "Error: Cannot divide by zero" in captured.out

    # Invalid operation handling
    def test_perform_calculation_invalid_operation_returns_none(self):
        """Test perform_calculation with invalid operation returns None."""
        result = perform_calculation(5, 3, '^')
        assert result is None

    def test_perform_calculation_invalid_operation_unknown_symbol(self):
        """Test perform_calculation with unknown operator."""
        result = perform_calculation(5, 3, '%')
        assert result is None

    # Zero operand tests
    def test_perform_calculation_with_zero_operands(self):
        """Test perform_calculation with zero as operand."""
        assert perform_calculation(0, 5, '+') == 5
        assert perform_calculation(5, 0, '-') == 5
        assert perform_calculation(0, 5, '*') == 0
        assert perform_calculation(0, 5, '/') == 0.0

    # Float operands
    def test_perform_calculation_with_floats(self):
        """Test perform_calculation with floating point numbers."""
        assert perform_calculation(1.5, 2.5, '+') == 4.0
        assert perform_calculation(5.0, 2.0, '/') == pytest.approx(2.5)

    # Parameterized orchestration tests
    @pytest.mark.parametrize("num1,num2,op,expected", [
        (2, 3, '+', 5),
        (5, 3, '-', 2),
        (3, 4, '*', 12),
        (6, 2, '/', 3.0),
        (-2, -3, '+', -5),
        (-5, -3, '-', -2),
        (0, 0, '+', 0),
        (0, 5, '*', 0),
    ])
    def test_perform_calculation_parametrized(self, num1, num2, op, expected):
        """Parametrized test for perform_calculation with valid operations."""
        assert perform_calculation(num1, num2, op) == expected

    @pytest.mark.parametrize("num1,op", [
        (5, '/'),
        (10, '/'),
        (-5, '/'),
        (0, '/'),
    ])
    def test_perform_calculation_division_by_zero_parametrized(self, num1, op):
        """Parametrized test for division by zero in perform_calculation."""
        assert perform_calculation(num1, 0, op) is None


class TestUserInputFunctions:
    """Test suite for user input functions using mocking."""

    # Tests for get_first_number
    def test_get_first_number_valid_integer(self):
        """Test get_first_number with valid integer input."""
        with patch('builtins.input', return_value='42'):
            result = get_first_number()
            assert result == 42.0

    def test_get_first_number_valid_float(self):
        """Test get_first_number with valid float input."""
        with patch('builtins.input', return_value='3.14'):
            result = get_first_number()
            assert result == pytest.approx(3.14)

    def test_get_first_number_negative(self):
        """Test get_first_number with negative number."""
        with patch('builtins.input', return_value='-42'):
            result = get_first_number()
            assert result == -42.0

    def test_get_first_number_invalid_then_valid(self):
        """Test get_first_number with invalid input followed by valid."""
        with patch('builtins.input', side_effect=['abc', '42']):
            with patch('builtins.print'):  # Suppress error message output
                result = get_first_number()
                assert result == 42.0

    # Tests for get_second_number
    def test_get_second_number_valid_integer(self):
        """Test get_second_number with valid integer input."""
        with patch('builtins.input', return_value='42'):
            result = get_second_number()
            assert result == 42.0

    def test_get_second_number_valid_float(self):
        """Test get_second_number with valid float input."""
        with patch('builtins.input', return_value='3.14'):
            result = get_second_number()
            assert result == pytest.approx(3.14)

    def test_get_second_number_zero(self):
        """Test get_second_number with zero."""
        with patch('builtins.input', return_value='0'):
            result = get_second_number()
            assert result == 0.0

    def test_get_second_number_invalid_then_valid(self):
        """Test get_second_number with invalid input followed by valid."""
        with patch('builtins.input', side_effect=['invalid', '5']):
            with patch('builtins.print'):  # Suppress error message output
                result = get_second_number()
                assert result == 5.0

    # Tests for get_operation
    def test_get_operation_addition(self):
        """Test get_operation returns addition operator."""
        with patch('builtins.input', return_value='+'):
            result = get_operation()
            assert result == '+'

    def test_get_operation_subtraction(self):
        """Test get_operation returns subtraction operator."""
        with patch('builtins.input', return_value='-'):
            result = get_operation()
            assert result == '-'

    def test_get_operation_multiplication(self):
        """Test get_operation returns multiplication operator."""
        with patch('builtins.input', return_value='*'):
            result = get_operation()
            assert result == '*'

    def test_get_operation_division(self):
        """Test get_operation returns division operator."""
        with patch('builtins.input', return_value='/'):
            result = get_operation()
            assert result == '/'

    def test_get_operation_invalid_then_valid(self):
        """Test get_operation with invalid input followed by valid."""
        with patch('builtins.input', side_effect=['invalid', '+']):
            with patch('builtins.print'):  # Suppress error message output
                result = get_operation()
                assert result == '+'

    def test_get_operation_invalid_operator(self):
        """Test get_operation rejects invalid operator."""
        with patch('builtins.input', side_effect=['^', '%', '+']):
            with patch('builtins.print'):  # Suppress error message output
                result = get_operation()
                assert result == '+'


class TestMainFunction:
    """Test suite for main orchestration function."""

    def test_main_addition_flow(self):
        """Test main function with addition operation."""
        with patch('builtins.input', side_effect=['5', '3', '+']):
            with patch('builtins.print') as mock_print:
                main()
                # Verify that result was printed
                output_calls = [str(call) for call in mock_print.call_args_list]
                output_text = ' '.join(output_calls)
                assert 'Result' in output_text or '8' in output_text

    def test_main_subtraction_flow(self):
        """Test main function with subtraction operation."""
        with patch('builtins.input', side_effect=['10', '3', '-']):
            with patch('builtins.print') as mock_print:
                main()
                output_calls = [str(call) for call in mock_print.call_args_list]
                output_text = ' '.join(output_calls)
                assert 'Result' in output_text or '7' in output_text

    def test_main_multiplication_flow(self):
        """Test main function with multiplication operation."""
        with patch('builtins.input', side_effect=['4', '5', '*']):
            with patch('builtins.print') as mock_print:
                main()
                output_calls = [str(call) for call in mock_print.call_args_list]
                output_text = ' '.join(output_calls)
                assert 'Result' in output_text or '20' in output_text

    def test_main_division_flow(self):
        """Test main function with division operation."""
        with patch('builtins.input', side_effect=['10', '2', '/']):
            with patch('builtins.print') as mock_print:
                main()
                output_calls = [str(call) for call in mock_print.call_args_list]
                output_text = ' '.join(output_calls)
                assert 'Result' in output_text or '5' in output_text

    def test_main_division_by_zero_flow(self):
        """Test main function with division by zero."""
        with patch('builtins.input', side_effect=['5', '0', '/']):
            with patch('builtins.print') as mock_print:
                main()
                output_calls = [str(call) for call in mock_print.call_args_list]
                output_text = ' '.join(output_calls)
                # Should show error, not result
                assert 'Error' in output_text or 'Cannot divide by zero' in output_text

    def test_main_with_floats(self):
        """Test main function with floating point numbers."""
        with patch('builtins.input', side_effect=['1.5', '2.5', '+']):
            with patch('builtins.print') as mock_print:
                main()
                output_calls = [str(call) for call in mock_print.call_args_list]
                output_text = ' '.join(output_calls)
                assert 'Result' in output_text or '4' in output_text

    def test_main_with_negative_numbers(self):
        """Test main function with negative numbers."""
        with patch('builtins.input', side_effect=['-5', '-3', '*']):
            with patch('builtins.print') as mock_print:
                main()
                output_calls = [str(call) for call in mock_print.call_args_list]
                output_text = ' '.join(output_calls)
                assert 'Result' in output_text or '15' in output_text


class TestEdgeCasesAndBoundaries:
    """Test edge cases and boundary conditions across all functions."""

    def test_very_large_number_addition(self):
        """Test addition with very large numbers."""
        result = add(1e100, 2e100)
        assert result == 3e100

    def test_very_small_number_addition(self):
        """Test addition with very small numbers."""
        result = add(1e-100, 2e-100)
        assert result == pytest.approx(3e-100)

    def test_precision_in_float_division(self):
        """Test float division precision."""
        result = divide(1, 3)
        assert result == pytest.approx(0.333333, rel=1e-5)

    def test_negative_zero_handling(self):
        """Test handling of negative zero."""
        result = add(0, -0)
        assert result == 0

    def test_multiple_operations_chaining(self):
        """Test chaining multiple operations."""
        result1 = add(2, 3)  # 5
        result2 = multiply(result1, 2)  # 10
        result3 = divide(result2, 5)  # 2
        assert result3 == 2.0

    def test_commutative_property_addition(self):
        """Test commutative property of addition."""
        result1 = add(5, 3)
        result2 = add(3, 5)
        assert result1 == result2

    def test_commutative_property_multiplication(self):
        """Test commutative property of multiplication."""
        result1 = multiply(5, 3)
        result2 = multiply(3, 5)
        assert result1 == result2

    def test_associative_property_addition(self):
        """Test associative property of addition."""
        result1 = add(add(1, 2), 3)
        result2 = add(1, add(2, 3))
        assert result1 == result2

    def test_associative_property_multiplication(self):
        """Test associative property of multiplication."""
        result1 = multiply(multiply(2, 3), 4)
        result2 = multiply(2, multiply(3, 4))
        assert result1 == result2

    def test_distributive_property(self):
        """Test distributive property: a*(b+c) = a*b + a*c."""
        a, b, c = 2, 3, 4
        result1 = multiply(a, add(b, c))
        result2 = add(multiply(a, b), multiply(a, c))
        assert result1 == result2

    def test_inverse_operations_addition_subtraction(self):
        """Test that addition and subtraction are inverses."""
        original = 10
        after_add = add(original, 5)
        back_to_original = subtract(after_add, 5)
        assert back_to_original == original

    def test_inverse_operations_multiplication_division(self):
        """Test that multiplication and division are inverses."""
        original = 10
        after_multiply = multiply(original, 5)
        back_to_original = divide(after_multiply, 5)
        assert back_to_original == pytest.approx(original)

    def test_identity_element_addition(self):
        """Test identity element for addition (adding 0)."""
        assert add(42, 0) == 42
        assert add(0, 42) == 42

    def test_identity_element_multiplication(self):
        """Test identity element for multiplication (multiplying by 1)."""
        assert multiply(42, 1) == 42
        assert multiply(1, 42) == 42

    def test_absorbing_element_multiplication(self):
        """Test absorbing element for multiplication (multiplying by 0)."""
        assert multiply(42, 0) == 0
        assert multiply(0, 42) == 0
