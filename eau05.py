############### String dans string ###############

import sys

import re

### Function ###

def include_string(a: str, b: str) -> bool:
    ...


def format_result_include(a: str, b: str) -> None:
    ...


def have_not_correct_number_of_arguments() -> None:

    if len(sys.argv) != 3:
        print("Error")
        exit()


def is_not_contain_letters(a: str, b:str) -> bool:
    
    match = re.search("[a-zA-Z]+", a and b)

    if match:
        return True
    

def error_arg(a: str, b: str) -> None:

    if is_not_contain_letters(a, b):
        return a and b
    else:
        print("Error")
        exit()


### Error ###

have_not_correct_number_of_arguments()

error_arg(sys.argv[1], sys.argv[2])

### Parsing ###

string_a = sys.argv[1]

string_b = sys.argv[2]

### Problem solving ###




### Result ###