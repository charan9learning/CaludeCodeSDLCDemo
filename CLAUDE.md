# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a demonstration project for Claude Code SDLC practices. It includes a simple Python calculator application that showcases best practices for software development lifecycle when working with Claude Code.

## Codebase Architecture

### Core Components

- **calculator.py** - Main application containing arithmetic operations and user interaction. Organized as:
  - Arithmetic functions: `add()`, `subtract()`, `multiply()`, `divide()`
  - Input validation: `is_valid_number()`, `get_operation()`, `get_first_number()`, `get_second_number()`
  - Orchestration: `perform_calculation()`, `main()`

The calculator follows a modular design with separate concerns for validation, computation, and UI interactions. Division by zero returns `None` rather than raising an exception.

## Common Development Tasks

### Running the Application

```bash
python calculator.py
```

Interactive mode prompts for two numbers and an operation, then displays the result.

### Testing

Currently, there are no automated tests. To add test coverage:

```bash
pytest calculator.py  # After adding pytest and test functions
```

## Code Patterns and Conventions

- Input validation is performed at the boundary (user input functions) before processing
- Operations return `None` to signal error conditions (e.g., division by zero)
- User-facing functions use docstrings explaining parameters and behavior
- Main logic separated into `main()` function, allowing easier testing
- String formatting uses f-strings for clarity

## Adding Features

When extending the calculator:
- Add new arithmetic functions alongside existing ones (`add`, `subtract`, etc.)
- Update the `valid_operations` list in `get_operation()` when adding operators
- Add corresponding conditions to `perform_calculation()`
- Consider whether new operations need special error handling (like division by zero)
