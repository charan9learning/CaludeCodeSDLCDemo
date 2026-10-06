---
name: calculator_testing_patterns
description: Testing patterns and best practices specific to the calculator codebase
metadata:
  type: reference
---

## Input Validation Testing (is_valid_number)

The calculator uses try/except pattern with float() conversion for validation. Test strategy covers:

**Happy Path:**
- Valid integers: positive, negative, zero
- Valid floats: positive, negative, zero
- Scientific notation: 1e5, -1.5e-3
- Boundary values: very large numbers, very small numbers

**Invalid Cases:**
- Empty strings
- Text strings (abc, hello42)
- Special characters (@#$%)
- Multiple decimal points (1.2.3)
- Whitespace only
- Operator symbols (+, -, *)

**Key Testing Pattern:** Use parametrized tests for comprehensive coverage of similar validation scenarios. This reduces code duplication while covering edge cases.

## Arithmetic Operations Testing

All arithmetic functions (add, subtract, multiply, divide) follow these patterns:

**Test Categories:**
1. Positive integers (happy path)
2. Negative integers
3. Mixed sign operations
4. Zero operands
5. Float operands
6. Very large/small numbers
7. Boundary conditions

**Error Handling Convention:**
- Division by zero returns None (not exception)
- Always test that divide(x, 0) is None for various x values
- Test that perform_calculation() catches None and prints error

## User Input Functions Testing (Using Mock/Patch)

For functions that call input():
- Use `patch('builtins.input', return_value=...)` to avoid interactive prompts
- For invalid-then-valid scenarios: use `side_effect=['invalid', 'valid']`
- Suppress error output with `patch('builtins.print')` during testing
- Test retry logic by providing multiple invalid inputs

## Main Function Testing

Main orchestrates input collection and calculation:
- Mock all input() calls with side_effect parameter
- Mock print() to capture output without side effects
- Test all operation types: +, -, *, /
- Test error cases: division by zero
- Test with various number types: integers, floats, negative

**Testing Approach:** Use patch with side_effect and mock_print with call_args_list to verify output.

## Mathematical Properties Testing

Test algebraic properties to catch calculation errors:
- Commutative property: a+b = b+a (addition, multiplication)
- Associative property: (a+b)+c = a+(b+c)
- Distributive property: a*(b+c) = a*b + a*c
- Inverse operations: add/subtract and multiply/divide
- Identity elements: 0 for addition, 1 for multiplication
- Absorbing element: 0 for multiplication

These tests catch subtle calculation bugs and are deterministic, not testing infrastructure.
