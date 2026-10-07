# Code Refactoring Skill

## Overview

This skill provides guidelines and best practices for refactoring code in the CaludeCodeSDLCDemo calculator project. Code refactoring improves code quality, maintainability, and performance without changing external behavior.

## When to Refactor

Refactor code when:
- Code is duplicated across multiple locations
- Functions are too large and handle multiple concerns
- Variable/function names are unclear or misleading
- Complex nested logic can be simplified
- Performance can be improved without sacrificing readability
- Test coverage is insufficient
- Code violates project conventions or patterns

## Do NOT Refactor When

- The task is to fix a specific bug (separate concern)
- You're adding a new feature (implement first, refactor later if needed)
- The code is working correctly and tests pass
- Refactoring would introduce backward compatibility issues
- There's insufficient test coverage to ensure safety

## Refactoring Strategy

### 1. Establish Baseline

Before refactoring:
```bash
# Run existing tests to ensure baseline
pytest test_calculator.py -v

# Check code coverage
pytest test_calculator.py --cov=calculator --cov-report=term-missing
```

### 2. Identify Refactoring Opportunities

Common patterns in calculator.py:
- **Duplicate input validation** - `get_first_number()` and `get_second_number()` are nearly identical
- **Switch statement in perform_calculation()** - Could use function dispatch dictionary
- **Mixed concerns in main()** - Orchestration logic mixed with UI formatting

### 3. Apply Safe Refactoring Techniques

#### A. Extract Functions
Break large functions into smaller, focused functions:

```python
# Before: Mixed concerns
def main():
    # ... 20 lines of code ...

# After: Separated concerns
def _get_calculation_inputs():
    """Get and validate inputs from user."""
    num1 = get_first_number()
    operation = get_operation()
    return num1, operation

def _display_result(num1, operation, result, num2=None):
    """Format and display calculation result."""
    print("=" * 40)
    if operation == 'cos':
        print(f"Result: cos({num1}) = {result}")
    else:
        print(f"Result: {num1} {operation} {num2} = {result}")
    print("=" * 40)
```

#### B. Remove Duplication
Consolidate similar functions:

```python
# Before: Two nearly identical functions
def get_first_number():
    """Get and validate the first number from user."""
    while True:
        user_input = input("Enter first number: ")
        if is_valid_number(user_input):
            return float(user_input)
        else:
            print("Error: Please enter a valid number.")

def get_second_number():
    """Get and validate the second number from user."""
    while True:
        user_input = input("Enter second number: ")
        if is_valid_number(user_input):
            return float(user_input)
        else:
            print("Error: Please enter a valid number.")

# After: Single parameterized function
def get_number(prompt_label="number"):
    """Get and validate a number from user with custom prompt."""
    while True:
        user_input = input(f"Enter {prompt_label}: ")
        if is_valid_number(user_input):
            return float(user_input)
        else:
            print("Error: Please enter a valid number.")
```

#### C. Use Function Dispatch
Replace long if-elif chains with dictionaries:

```python
# Before: Long conditional chain
def perform_calculation(num1, num2, operation):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
        if result is None:
            print("Error: Cannot divide by zero.")
            return None
        return result
    elif operation == 'cos':
        return cosine(num1)

# After: Function dispatch dictionary
OPERATIONS = {
    '+': lambda n1, n2: add(n1, n2),
    '-': lambda n1, n2: subtract(n1, n2),
    '*': lambda n1, n2: multiply(n1, n2),
    '/': _safe_divide,
    'cos': lambda n1, n2: cosine(n1),
}

def _safe_divide(num1, num2):
    """Safely divide with error handling."""
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    return divide(num1, num2)

def perform_calculation(num1, num2, operation):
    return OPERATIONS.get(operation, lambda *args: None)(num1, num2)
```

#### D. Improve Naming
Use clear, descriptive names:

```python
# Before: Unclear
def is_valid_number(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False

# After: More explicit (if desired, though this is already clear)
def is_float_convertible(input_string):
    """Check if input string can be converted to a float."""
    try:
        float(input_string)
        return True
    except ValueError:
        return False
```

### 4. Maintain Test Coverage

After each refactoring step:

```bash
# Run tests
pytest test_calculator.py -v

# Verify no tests broke
pytest test_calculator.py --tb=short

# Check coverage didn't decrease
pytest test_calculator.py --cov=calculator --cov-report=term-missing
```

### 5. Create Atomic Commits

Each refactoring should be a separate commit:

```bash
# Commit each refactoring step
git add .
git commit -m "Refactor: Extract input validation into reusable function"

# Continue with next refactoring
git add .
git commit -m "Refactor: Use function dispatch dictionary for operations"
```

## Refactoring Checklist

Before submitting a refactor:

- [ ] All tests pass (`pytest test_calculator.py -v`)
- [ ] Code coverage maintained or improved
- [ ] No external behavior changed (functions work the same from caller's perspective)
- [ ] Variable/function names are clear and descriptive
- [ ] Code follows project conventions (PEP 8, docstrings, etc.)
- [ ] Each commit represents one logical refactoring
- [ ] Documentation updated if needed (CLAUDE.md, docstrings)
- [ ] No dead code left behind

## Calculator-Specific Refactoring Opportunities

### High Priority
1. **Consolidate get_first_number() and get_second_number()** into `get_number(prompt)`
2. **Extract operation logic** from `perform_calculation()` into a dispatch dictionary
3. **Separate display logic** from `main()` function

### Medium Priority
1. **Add logging** for debugging calculator operations
2. **Extract magic strings** ('+', '-', etc.) into constants
3. **Create Operation enum** for type safety

### Low Priority
1. **Add result formatting** as a separate function
2. **Create Calculator class** to encapsulate state (if needed)
3. **Optimize trigonometric calculations** with memoization

## Common Mistakes to Avoid

❌ **Don't refactor to patterns you don't need yet**
- Three similar lines is better than premature abstraction
- Only consolidate when there are clear maintenance benefits

❌ **Don't change behavior while refactoring**
- Refactoring should not alter how functions work
- If you need to change behavior, do it separately with tests

❌ **Don't skip tests**
- Always run tests before and after refactoring
- Refactoring with no tests is dangerous

❌ **Don't ignore performance**
- Some refactorings (like dispatch dicts) trade performance for readability
- Measure before and after if performance matters

❌ **Don't refactor untested code**
- Code must have tests to safely refactor
- Add tests first if needed

## Tools and Commands

```bash
# Run full test suite with coverage
pytest test_calculator.py -v --cov=calculator --cov-report=html

# Run specific test class
pytest test_calculator.py::TestArithmeticOperations -v

# Check code style
python3 -m flake8 calculator.py --max-line-length=100

# Format code (if Black is installed)
python3 -m black calculator.py --line-length=100
```

## Resources

- PEP 8 Style Guide: https://www.python.org/dev/peps/pep-0008/
- Refactoring Techniques: https://refactoring.guru/refactoring
- Clean Code Principles: https://www.oreilly.com/library/view/clean-code-a/9780136083238/
- Project CLAUDE.md: Code patterns and conventions

## Next Steps

To apply refactoring:

1. Choose one refactoring opportunity from the high-priority list
2. Run tests to establish baseline
3. Apply the refactoring technique
4. Run tests again to verify nothing broke
5. Create an atomic commit with clear message
6. Document any changes in CLAUDE.md if needed

## Example Refactoring Session

```bash
# 1. Baseline
pytest test_calculator.py -v --cov=calculator

# 2. Make changes to calculator.py
# (e.g., consolidate get_first_number and get_second_number)

# 3. Verify tests still pass
pytest test_calculator.py -v

# 4. Verify behavior hasn't changed
python3 -c "from calculator import *; print(add(2, 3))"  # Should print 5

# 5. Commit
git add calculator.py
git commit -m "Refactor: Consolidate input functions into get_number()"

# 6. Update documentation
# Edit CLAUDE.md if needed
git add CLAUDE.md
git commit -m "docs: Update CLAUDE.md with new input function signature"
```

---

**Remember**: The goal of refactoring is to improve code quality and maintainability while preserving behavior. When in doubt, run the tests!
