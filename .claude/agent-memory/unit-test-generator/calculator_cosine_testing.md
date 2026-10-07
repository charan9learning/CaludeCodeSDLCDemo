---
name: calculator_cosine_testing_patterns
description: Testing patterns and strategies for cosine function and trigonometric operations
metadata:
  type: reference
---

## Cosine Function Testing Patterns

### Mathematical Properties Tested

1. **Exact Values**: cosine(0)=1, cos(π)=-1, cos(π/2)≈0, cos(π/4)≈0.707
2. **Even Function Property**: cos(-x) = cos(x) for any angle
3. **Periodicity**: cos(x) = cos(x + 2π) - tested across single and multiple periods
4. **Small Angle Behavior**: cos(x) ≈ 1 for very small x values
5. **Large Angle Behavior**: Due to periodicity, cos(large_angle) reduces to standard range

### Precision Handling

- Use `pytest.approx()` with absolute tolerance for values near 0: `pytest.approx(0.0, abs=1e-10)`
- Use relative tolerance for general comparisons: `pytest.approx(expected, rel=1e-10)`
- Use absolute tolerance for values near 1: `pytest.approx(1.0, abs=1e-10)`

### Test Organization Strategy

- **TestCosineFunction** (42 tests): Core mathematical properties
  - Exact values (6 tests)
  - Even function property (3 tests)
  - Periodicity (4 tests)
  - Small angles (2 tests)
  - Large angles (2 tests)
  - Additional standard angles (4 tests)
  - Parameterized tests (9 tests + 6 parametrized even function + multiple periodicity)

- **TestCosineInPerformCalculation** (11 tests): Integration with orchestration function
  - Tests that perform_calculation routes to cosine correctly
  - Verifies num2 parameter is ignored for cosine operations
  - Parameterized tests for various angles

- **TestGetOperationWithCosine** (10 tests): Input validation
  - Accepts 'cos' as valid operation
  - Rejects typos and case variations (COS, Cos, cosine, etc.)
  - Validates error message mentions cosine
  - Tests invalid ops still rejected in presence of cosine

- **TestMainFunctionWithCosine** (10 tests): End-to-end workflow
  - Only requests one number for cosine (not two)
  - Output format verification
  - Binary operations still work correctly
  - Parameterized tests with various angles

### Key Testing Insights

1. **Unary vs Binary Operations**: Cosine is unary (one operand) while +,-,*,/ are binary - requires special main() handling
2. **Float Precision**: Trigonometric functions need careful precision handling due to floating-point representation
3. **Periodicity Testing**: Must verify cos(x) = cos(x + 2π) at multiple scales
4. **Operation Validation**: New operations must integrate seamlessly with existing input validation

### Edge Cases Covered

- Zero input (boundary value)
- Multiples of π (mathematically significant)
- Negative angles (verifies even property)
- Very small angles (precision edge case)
- Very large angles (periodicity verification)
- Angles with special significance (π/6, π/4, π/3, etc.)

### Total Test Count for Cosine Support

- 42 tests in TestCosineFunction
- 11 tests in TestCosineInPerformCalculation
- 10 tests in TestGetOperationWithCosine
- 10 tests in TestMainFunctionWithCosine
- **Total: 73 new tests for cosine support**
- **Existing tests: 152** (unchanged, fully compatible)
- **Grand total: 225 tests**
