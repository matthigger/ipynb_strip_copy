# ipynb_strip_copy

Command line tool to detect text in a jupyter notebook cell and process 
accordingly (delete, clear or delete all cells which don't contain that 
text).  Our motivation is to allow users to maintain a "rubric" `ipynb` file from 
which the "solution" and "student" copies can be created quickly.

## Installation

    pip install ipynb_strip_copy

## Usage / Example

Open up [test_cli_hw_rub.ipynb](https://github.com/matthigger/ipynb_strip_copy/blob/main/test/test_cli_hw_rub.ipynb) and use the 
command line interface via the jupyter magic command `!`:

    !python -m ipynb_strip_copy test_cli_hw.ipynb -t hw

Which:
- creates `test_cli_hw_sol.ipynb` by:
    - removing any cell with the string 'rubric'
    - raising an error on any cell with the string 'todo'
- creates `test_cli_hw.ipynb` by:
    - removing any cell with the string 'rubric'
    - removing any cell with the string 'solution'
    - raising an error on any cell with the string 'todo'

See the [prep_hw()](https://github.com/matthigger/ipynb_strip_copy/blob/main/ipynb_strip_copy/prep.py) for 
implementation 
details.

## Notes
- string matching is case-insensitive