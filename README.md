# LeetCode Contest

Python solutions for LeetCode weekly and biweekly contests, including templates that can be directly used in LeetCode solutions.

Each problem file is self-contained: it includes the problem statement, constraints, solution, and runnable examples.

This project is under active maintenance, solutions will be posted shortly after each contest.


## Running a solution

Run any problem file directly from the repository root:

```bash
python3 "Weekly Contest/Weekly Contest 519/4052. Cyclically Shift Rows and Columns.py"
```

The `__main__` section at the bottom of each file runs the examples from the problem statement.

## Optional setup

Most solutions use only the Python standard library. To install the additional dependency used by some solutions:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Templates

The [`Templates`](./Templates) directory contains reusable implementations for common contest techniques, including:

- Binary indexed trees
- Segment trees and lazy segment trees
- Sparse tables
- Union-find
- Prime utilities
- Combinations
- XOR basis

## File format

New solutions follow the structure in [`format.py`](./format.py):

1. Problem statement, examples, and constraints
2. Required imports
3. `Solution` class and method
4. Runnable example cases
