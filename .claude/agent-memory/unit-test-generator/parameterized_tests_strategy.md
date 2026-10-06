---
name: parameterized_tests_strategy
description: Effective use of pytest parameterization for the calculator codebase
metadata:
  type: reference
---

## Parameterized Testing for Calculator Functions

The calculator has many similar test cases (e.g., add(1,2)=3, add(-1,-2)=-3, add(0,5)=5). Use `@pytest.mark.parametrize` to cover these efficiently without code duplication.

## Implementation Pattern

**Basic Structure:**
```python
@pytest.mark.parametrize("input1,input2,expected", [
    (val1, val2, result1),
    (val1, val2, result2),
])
def test_function_parametrized(self, input1, input2, expected):
    """Clear docstring explaining what is being tested."""
    assert function(input1, input2) == expected
```

## Application to Calculator

**For is_valid_number():**
- Group 10+ valid inputs in one parametrized test
- Group 8+ invalid inputs in another parametrized test
- Reduces 18+ individual tests to 2 parametrized tests with clear coverage

**For arithmetic functions (add, subtract, multiply, divide):**
- Group 5-7 representative cases per operation per function
- Test cases should cover: positive, negative, mixed sign, zero operands, floats
- Example: test_add_parametrized with 5 cases, test_multiply_parametrized with 5 cases

**For division by zero:**
- Create parametrized test across different numerators: [5, -5, 0, 0.5, -0.5]
- Efficiently verify all divide(x, 0) is None cases

**For perform_calculation():**
- Parametrize across all 4 valid operations with representative numbers
- Parametrize division by zero cases across different numerators
- Keep parametrization semantic (group by operation type, not random)

## Benefits Observed

1. **Code reduction:** 25+ individual tests → 12 parametrized tests covering same cases
2. **Maintainability:** Add new test case by adding one line to parameter list
3. **Clarity:** Test name + parameter values clearly show what's being tested
4. **Coverage:** Easier to ensure all relevant combinations are tested

## Semantic Organization

Group parametrized tests by what is varying:
- Test across different operations: `@pytest.mark.parametrize("operation", ['+', '-', '*', '/'])`
- Test across different input types: `@pytest.mark.parametrize("input_val", [5, -5, 0, 3.14])`
- Test multiple dimensions: `@pytest.mark.parametrize("num1,num2,op,expected", [(...),...])` for complex scenarios

## Trade-off

Parameterized tests are most effective when:
- Testing the same function with many similar inputs
- The test logic is identical, only inputs vary
- You have 5+ test cases that would otherwise be repetitive

Avoid parameterization when:
- Each test has different setup/assertions (use test classes or separate tests)
- Testing fundamentally different scenarios (keep them separate for clarity)
