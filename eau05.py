############### String dans string ###############

import sys

import re

### Function ###

def include_string(a: str, b: str) -> bool:

    if a.find(b) == -1:
        return False
    else:
        return True


def format_result_include(a: str, b: str) -> None:
    
    if include_string(a, b):
        print("true")
        exit()
    else:
        print("false")
        exit()


def have_not_correct_number_of_arguments() -> None:

    if len(sys.argv) != 3:
        print("Error")
        exit()


def is_not_contain_letters(a: str, b:str) -> bool:
    
    match = re.search("[a-zA-Z]+", a and b)

    if match:
        return True


def is_not_correct_length(a: str, b: str) -> bool:

    if len(a) < len(b):
        return True


def error_arg(a: str, b: str) -> None:

    if is_not_contain_letters(a, b):
        pass
    else:
        print("Error")
        exit()

    if is_not_correct_length(a, b):
        print("Error")
        exit()


### Error ###

have_not_correct_number_of_arguments()

error_arg(sys.argv[1], sys.argv[2])

### Parsing ###

string_a = sys.argv[1]

string_b = sys.argv[2]

### Problem solving ###

final_result = format_result_include(string_a, string_b)

### Result ###

print(final_result)