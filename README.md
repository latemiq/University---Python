# 🐍 Python Learning Tasks

A structured, menu-driven Python program covering four fundamental areas of Python programming. Each section contains a set of hands-on exercises designed for students learning Python from scratch.

---

## 📚 Contents

- [Overview](#overview)
- [How to Run](#how-to-run)
- [Sections](#sections)
  - [Section 1 – Data Types, Variables & Conversions](#section-1--data-types-variables--conversions)
  - [Section 2 – Conditional Statements](#section-2--conditional-statements)
  - [Section 3 – Loops](#section-3--loops)
  - [Section 4 – Functions](#section-4--functions)
- [Requirements](#requirements)

---

## Overview

This project is a collection of **57 programming exercises** organized into four sections that progressively build Python skills. The program runs interactively in the terminal — the user selects a section and then a task number to execute it.

---

## How to Run

```bash
python zadania.py
```

No external libraries required. The program uses only Python's built-in `math` and `random` modules.

---

## Sections

### Section 1 – Data Types, Variables & Conversions
*20 tasks*

Covers the basics of working with different data types, type conversions, arithmetic operations, string manipulation, and randomness.

| # | Task | Topics |
|---|------|--------|
| 1 | BMI Calculator | `int`, `float`, arithmetic, f-strings |
| 2 | Family Income per Person | variables, division, formatting |
| 3 | Height Conversion (cm → feet & inches) | `//`, `%` operators |
| 4 | Distance to the Horizon | `math.sqrt()`, formula |
| 5 | Circle Area & Circumference | `math.pi`, arithmetic |
| 6 | Transport Cost Calculator | multi-variable input, arithmetic |
| 7 | VAT Calculator | percentage, rounding |
| 8 | Tax Exemption Check | comparison operator, boolean |
| 9 | Password Validator | `len()`, boolean output |
| 10 | License Plate Checker (Kraków) | string slicing, `or` operator |
| 11 | Motorway Speed Verification | `and` operator, range check |
| 12 | Employee Data Extraction | string slicing, indexing |
| 13 | Phone Number Formatter | string slicing, `isdigit()` |
| 14 | SWIFT/BIC Code Extractor | string slicing |
| 15 | Variable Swap | temporary variable |
| 16 | Dice Roll Simulator (vs. computer) | `random.randint()`, boolean |
| 17 | Sum of Three Dice Rolls | list comprehension, `sum()` |
| 18 | Number Base Conversion | `bin()`, `hex()` |
| 19 | Character Code Translator | `ord()` |
| 20 | Hidden Word Decoder | `chr()`, string joining |

---

### Section 2 – Conditional Statements
*15 tasks*

Covers decision-making using `if`, `elif`, `else`, and logical operators (`and`, `or`, `not`).

| # | Task | Topics |
|---|------|--------|
| 1 | Vehicle Speed Check | `if/else` |
| 2 | Even or Odd Number | `%` operator, `if/else` |
| 3 | Payment Terminal Simulation | balance comparison |
| 4 | Test Pass/Fail | percentage calculation, `if/else` |
| 5 | Salary with Bonus | conditional multiplication |
| 6 | Clothing Size Description | `if/elif/else` |
| 7 | Four-Operation Calculator | operator selection with `elif` |
| 8 | Fuel Consumption by Drive Mode | `elif`, dictionary-style logic |
| 9 | Quarter of the Year | range checks with `elif` |
| 10 | Age Classification | Child / Teen / Adult / Senior |
| 11 | User Login | `and` operator |
| 12 | Discount Eligibility | `or` operator |
| 13 | Are Both People Adults? | `and` operator |
| 14 | Non-Negative Number Check | `not` operator |
| 15 | EAN-13 Barcode Validator | `len()`, `isdigit()`, string slicing |

---

### Section 3 – Loops
*12 tasks*

Covers iteration using `for` and `while` loops, accumulators, and loop control.

| # | Task | Topics |
|---|------|--------|
| 1 | Print Numbers 1–10 | `for` loop, `range()` |
| 2 | Even Numbers 1–20 (one line) | `range()` with step, `end=""` |
| 3 | Sum of Numbers 1 to n | accumulator pattern |
| 4 | Print Each Letter of a Word | iterating over a string |
| 5 | Multiplication Table 1–5 | nested `for` loops |
| 6 | Count Characters Without `len()` | manual counter |
| 7 | Average of 5 Numbers | `for` loop, division |
| 8 | Largest of 7 Numbers | tracking max value |
| 9 | Sum Until Zero | `while` loop, `break` |
| 10 | Horizontal Star Chart | string repetition |
| 11 | Count Occurrences of Letter 'a' | character comparison |
| 12 | Computer Guesses User's Number | `while` loop, `random.randint()` |

---

### Section 4 – Functions
*10 tasks*

Covers defining and calling functions, arguments, return values, scope, recursion, and code organization.

| # | Task | Topics |
|---|------|--------|
| 1 | Built-in Functions | `max()`, `min()`, `len()` |
| 2 | Define a Function with `return` | `evenOdd(x)` function |
| 3 | Functions from Modules | `math.sqrt()`, `math.log()`, `random.randint()` |
| 4 | Default Arguments | `def myFun(x, y=50)` |
| 5 | Keyword Arguments | named parameter passing |
| 6 | Mutable vs. Immutable Objects | pass by object reference |
| 7 | Nested Functions | inner function, variable scope |
| 8 | Recursion | `factorial(n)` with base case |
| 9 | Code Organization into Modules | `converters.py`, `import` |
| 10 | `if __name__ == "__main__"` | program entry point pattern |

---

## Requirements

- Python **3.6+**
- No external packages needed

```bash
# Check your Python version
python --version
```

---

## Project Structure

```
zadania.py     # Main program file — all 57 tasks
README.md      # This file
```

---

*Created as part of a Python programming course covering the fundamentals of the language.*
