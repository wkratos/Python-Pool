*This project has been created as part of the 42 curriculum by wkratos.*

# PythonPool

A structured collection of Python exercises completed across eleven progressive modules, from basic syntax and control flow to object-oriented design, package management, data validation, functional programming, closures, and decorators.

---

## Overview

PythonPool documents my progression through Python by combining focused exercises with small themed applications.

The repository covers:

- Python syntax and control structures
- Functions and recursion
- Object-oriented programming
- Inheritance and encapsulation
- Exception handling
- Command-line arguments
- Built-in collections
- Generators and data streams
- File and stream management
- Abstract classes and protocols
- Packages and import systems
- Virtual environments and dependencies
- Environment variables
- Pydantic data validation
- Functional programming
- Closures and decorators

---

## Repository Structure

```text
PythonPool/
├── Module00/
├── Module01/
├── Module02/
├── Module03/
├── Module04/
├── Module05/
├── Module06/
├── Module07/
├── Module08/
├── Module09/
├── Module10/
├── .gitignore
└── README.md
```

Each module contains independent exercises that focus on a specific group of Python concepts.

---

## Module Overview

| Module | Main Concepts |
|---|---|
| `Module00` | Python basics, input/output, conditions, loops, functions, recursion and type hints |
| `Module01` | Classes, objects, attributes, methods, encapsulation, inheritance, class methods and static methods |
| `Module02` | Exceptions, custom exceptions, raising errors, cleanup with `finally` and error-safe program design |
| `Module03` | Command-line arguments, lists, tuples, sets, dictionaries, generators and data analysis |
| `Module04` | File handling, streams, context management, archive creation and safe resource cleanup |
| `Module05` | Abstract base classes, polymorphism, protocols, reusable processors, pipelines and advanced type hints |
| `Module06` | Python packages, modules, imports, relative imports, nested packages and circular-import management |
| `Module07` | Advanced OOP, abstract interfaces, multiple inheritance, factories, strategies and tournament systems |
| `Module08` | Virtual environments, package installation, dependency management and environment variables |
| `Module09` | Structured data models, Pydantic validation, enums, field constraints and model-level validation |
| `Module10` | Lambdas, higher-order functions, closures, scope, `functools`, decorators and function composition |

---

## Highlights

### Object-Oriented Programming

The modules gradually introduce:

- class creation;
- instance and class attributes;
- inheritance;
- encapsulation;
- abstract base classes;
- multiple inheritance;
- polymorphism;
- factory and strategy design patterns.

Module07 applies these concepts through a card-game system containing cards, decks, combat interfaces, factories, strategies, a game engine and a tournament platform.

### Error Handling

Module02 explores reliable error management through:

- `try` and `except`;
- multiple exception types;
- custom exception hierarchies;
- explicit `raise` statements;
- cleanup using `finally`;
- validation before state changes.

### Generators and Data Processing

The repository includes:

- generator-based streams;
- score and inventory analytics;
- numeric and text processors;
- abstract data streams;
- reusable processing pipelines;
- input, transformation and output stages.

### Packages and Imports

Module06 builds a complete nested package structure:

```text
alchemy/
├── elements.py
├── potions.py
├── grimoire/
│   ├── spellbook.py
│   └── validator.py
└── transmutation/
    ├── basic.py
    └── advanced.py
```

It demonstrates:

- absolute imports;
- relative imports;
- package initialization;
- aliases;
- nested modules;
- circular dependency considerations.

### Functional Programming

Module10 focuses on:

- lambda expressions;
- `map`, `filter` and `sorted`;
- higher-order functions;
- closures and `nonlocal`;
- `functools.reduce`;
- function composition;
- reusable decorators;
- preserving metadata with `functools.wraps`.

---

## Requirements

Most exercises only require:

```text
Python 3.10+
```

Some later modules use additional packages:

```bash
pip install pandas numpy matplotlib requests python-dotenv pydantic
```

Using a virtual environment is recommended:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy matplotlib requests python-dotenv pydantic
```

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install pandas numpy matplotlib requests python-dotenv pydantic
```

---

## Running an Exercise

Each exercise can generally be executed independently.

Example:

```bash
python3 Module00/ex0/ft_hello_garden.py
```

Run an object-oriented exercise:

```bash
python3 Module01/ex6/ft_garden_analytics.py
```

Run the card game engine from Module07:

```bash
cd Module07
python3 -m ex3.main
```

Run a functional-programming exercise:

```bash
python3 Module10/ex4/decorator_mastery.py
```

Some exercises accept command-line arguments:

```bash
python3 Module03/ex0/ft_command_quest.py hello python 42
```

---

## Environment Variables

Module08 contains an environment-configuration exercise.

Create the local environment file from the example:

```bash
cp Module08/ex2/.env.example Module08/ex2/.env
```

Then edit the values before running:

```bash
python3 Module08/ex2/oracle.py
```

The real `.env` file is intentionally excluded from Git.

---

## Learning Objectives

The main objectives of this repository were to:

- understand Python syntax and conventions;
- write readable and reusable functions;
- model systems with classes and inheritance;
- handle errors safely;
- work with Python collections effectively;
- process data through generators and pipelines;
- organize code into packages and modules;
- manage project environments and dependencies;
- validate structured data;
- understand functional programming techniques;
- build progressively larger Python applications.

---

## Notes

- Every module represents a different stage of the learning process.
- Exercises are intentionally kept separate to preserve their original scope.
- The repository contains educational implementations rather than one single production application.
- Some programs use themed scenarios such as gardens, games, alchemy, space stations and magic to demonstrate technical concepts.

---

## Author

**wkratos — `wkratos`**

42 Network / 1337 student.