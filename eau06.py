############### Majuscule sur deux ###############

import sys

import re

### Function ###

def transform_one_of_two_letter_in_upper(arg: str) -> str:

    new_string = ""

    count = 0

    for char in arg:

        if re.match(r"[a-zA-Z]", char):

            if count % 2 == 0:
                new_string += char.upper()
            else:
                new_string += char

            count += 1

        else:
            new_string += char

    return new_string

            
def have_not_correct_number_of_arguments() -> None:

    if len(sys.argv) != 2:
        print("Error")
        exit()


def is_not_contain_letters(a: str) -> bool:
    
    if re.search(r"[a-zA-Z]+", a):
        return True


def error_arg(a: str) -> None:

    if is_not_contain_letters(a):
        pass
    else:
        print("Error")
        exit()


### Error ###

have_not_correct_number_of_arguments()

error_arg(sys.argv[1])

### Parsing ###

string_to_transform = sys.argv[1]

### Problem solving ###

result = transform_one_of_two_letter_in_upper(string_to_transform)

### Result ###

print(result)