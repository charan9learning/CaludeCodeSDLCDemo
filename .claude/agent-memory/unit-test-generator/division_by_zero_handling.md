---
name: division_by_zero_handling
description: Calculator codebase convention for handling division by zero
metadata:
  type: reference
---

## Error Handling Convention

**Rule:** Division by zero returns `None` rather than raising an exception.

**Why:** Follows the codebase's error-handling pattern of using None to signal error conditions instead of exceptions. This allows graceful handling at the orchestration level.

**How to apply:**

1. **divide() function:** Always test `divide(x, 0) is None` for any numerator x
   - Positive numerator: `divide(5, 0) is None`
   - Negative numerator: `divide(-5, 0) is None`
   - Zero numerator: `divide(0, 0) is None`

2. **perform_calculation() function:** When operation is '/', catches the None return from divide() and:
   - Prints error message: "Error: Cannot divide by zero."
   - Returns None to caller

3. **Testing strategy:** 
   - Unit test the divide() function returns None
   - Unit test perform_calculation() handles the None and prints error message using capsys fixture
   - End-to-end test the error message appears when dividing by zero

4. **Never change this behavior** — it's a consistent error-handling pattern used throughout the codebase.

## Related Pattern

The codebase uses None returns to signal errors at operation level, then checks for None at the orchestration level (perform_calculation). This pattern allows functions to be composable while maintaining clear error semantics.
