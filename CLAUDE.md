# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands
- Run Python file: `python filename.py`
- Test a solution: `python -m pytest test_filename.py::test_function_name -v`
- All tests: `python -m pytest`
- Type checking: `mypy filename.py`
- Lint code: `flake8 filename.py`

## Code Style
- Use type annotations for all function parameters and return values
- Follow PEP 8 conventions (4-space indentation, 79 char line length)
- Import order: standard library → third-party modules → local modules
- Class/Function naming: CamelCase for classes, snake_case for functions/variables
- Use meaningful variable names that reflect purpose
- Include docstrings for all functions using triple quotes
- Handle edge cases explicitly (empty inputs, None values, etc.)
- Use constants for magic numbers
- Prefer list comprehensions over loops when appropriate
- Organize leetcode solutions by pattern/data structure