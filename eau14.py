############### Par ordre Ascii ###############

import sys

from typing import List

### Function ###

def ascii_sort(arguments: List[str]) -> List[str]:

    ascii_dict = {}

    for element in arguments:

        first_char = element[0]
        code_ascii = ord(first_char)

        if code_ascii not in ascii_dict:
            ascii_dict[code_ascii] = [element]
        else:
            ascii_dict[code_ascii].append(element)

    ascii_list_sorted = sorted(ascii_dict.keys())

    final_list = []

    for ascii_code in ascii_list_sorted:
        final_list.extend(ascii_dict[ascii_code])

    return final_list


def print_correct(ascii_array: List[str]) -> int:

    for element in ascii_array:
        print(f"{element} ", end="")
    
    print("")
    exit()


def incorrect_argument_count() -> None:

    if len(sys.argv) <= 2:
        print("Error")
        exit()


def error_argument() -> None:

    for element in sys.argv[1:]:

        if element.isascii():
            pass
        else:
            print("Error")
            exit()


### Error ###

incorrect_argument_count()

error_argument()

### Parsing ###

list_argument = sys.argv[1:]

### Problem solving ###

sorted_ascii = ascii_sort(list_argument)

correct_sentence = print_correct(sorted_ascii)

### Result ###

print(sorted_ascii)