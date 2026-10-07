# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a demonstration project for Claude Code SDLC practices. It includes a simple Python calculator application that showcases best practices for software development lifecycle when working with Claude Code.

## Codebase Architecture

### Core Components

**calculator.py** - Main application with clean separation of concerns:

#### Arithmetic Operations Layer
- `add()`, `subtract()`, `multiply()`, `divide()` - Basic arithmetic functions
- `cosine()` - Trigonometric function (operates on radians)

#### Input Validation Layer
- `is_valid_number()` - Validates numeric input strings
- `get_number()` - Reusable function for getting and validating user numbers
- `get_first_number()`, `get_second_number()` - Convenience wrappers around `get_number()`
- `get_operation()` - Validates and returns user-selected operation

#### Calculation & Display Layer
- `OPERATIONS` - Dictionary mapping operators to their implementation functions
- `_safe_divide()` - Division with error handling (private helper)
- `perform_calculation()` - Uses function dispatch to execute operations
- `_display_result()` - Formats and displays calculation results (private helper)

#### Orchestration Layer
- `main()` - Coordinates user interaction and calculation flow

### Design Patterns

- **Function Dispatch Dictionary**: `OPERATIONS` dict eliminates long if-elif chains
- **Separation of Concerns**: Input validation, calculation, and display are independent
- **Error Handling**: Operations return `None` for error conditions (e.g., division by zero)
- **DRY Principle**: Input functions consolidated into single `get_number()` implementation
- **Private Helpers**: Internal functions prefixed with `_` to indicate private use

## Common Development Tasks

### Running the Application

```bash
python calculator.py
```

Interactive mode prompts for numbers and an operation, then displays the result.

### Testing

Comprehensive test suite with 228 tests (226 passing):

```bash
# Run all tests
pytest test_calculator.py -v

# Run with coverage report
pytest test_calculator.py --cov=calculator --cov-report=term-missing

# Run specific test class
pytest test_calculator.py::TestArithmeticOperations -v
```

Test coverage includes:
- Validation functions (36 tests)
- Arithmetic operations (44 tests)
- Calculation orchestration (21 tests)
- User input handling (15 tests)
- Main function workflow (8 tests)
- Edge cases and boundaries (27 tests)
- Cosine function (73 tests)

## Code Patterns and Conventions

- Input validation at boundary layer before processing
- Operations return `None` to signal error conditions
- All public functions have docstrings
- Private helpers prefixed with `_` (e.g., `_safe_divide()`)
- String formatting uses f-strings
- Function dispatch dictionary for extensible operation handling
- Trigonometric functions operate on radians (not degrees)

## Adding Features

When extending the calculator:

1. **New arithmetic function**:
   ```python
   def sine(num1):
       """Calculate sine of a number (in radians)."""
       return math.sin(num1)
   ```

2. **Add to operations dictionary**:
   ```python
   OPERATIONS['sin'] = lambda n1, n2: sine(n1)
   ```

3. **Update get_operation()**:
   ```python
   valid_operations = ['+', '-', '*', '/', 'cos', 'sin']
   ```

4. **Update main()** if operation is unary (like cosine):
   ```python
   if operation in UNARY_OPERATIONS:  # Handle single operand
   else:  # Handle binary operations
   ```

5. **Add tests** in test_calculator.py for new functionality

6. **Update CLAUDE.md** with new operation details

### Refactoring Guidelines

See `.claude/skills/code-refactor/SKILL.md` for detailed refactoring practices.

Common refactoring opportunities:
- Extract related logic into helper functions (like `_safe_divide()`)
- Use function dispatch for replacing long conditional chains
- Consolidate similar functions with parameterization (like `get_number()`)
- Keep private helpers private with `_` prefix

## Test Coverage

Current test coverage:
- ✅ 100% function coverage
- ✅ 100% branch coverage  
- ✅ All edge cases and error conditions tested
- ✅ Mathematical properties validated (periodicity, even function property, etc.)
- ✅ User input mocking for interactive functions

Known test limitations:
- NaN/infinity edge cases due to Python's `float()` behavior
- Floating-point precision for very large numbers
