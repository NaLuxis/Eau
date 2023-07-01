############### Entre min et max ###############

import sys

from typing import List

### Function ###

def number_sort(argument_1: int, argument_2: int) -> List[int]:

    argument_1 = sys.argv[1]
    argument_2 = sys.argv[2]

    list_to_sort = [argument_1, argument_2]

    sorted_list = sorted(list_to_sort)

    return sorted_list


def range_min_max(min_max_list: List[int]) -> List[int]:
    
    start_number = int(min_max_list[0])
    end_number = int(min_max_list[1])

    number_list = []

    while start_number < end_number:
        number_list.append(start_number)
        start_number += 1
    
    return number_list

def print_correct(argument_list: List[int]) -> None:

    for number in argument_list:
        print(f"{number} ", end="")
    
    print("")
    exit()

def incorrect_argument_count() -> None:

    if len(sys.argv) != 3:
        print("Error")
        exit()


def is_number(target: any) -> bool:

    if not str(target).isdigit():
        return True


def is_equal(number_1: int, number_2: int) -> bool:

    if number_1 == number_2:
        return True


def error_argument() -> None:

    if not is_number(sys.argv[1]) and not is_number(sys.argv[2]):
        pass
    else:
        print("Error")
        exit()
    
    if is_equal(sys.argv[1], sys.argv[2]):
        print("Error")
        exit()


### Error ###

incorrect_argument_count()

error_argument()

### Parsing ###

first_number = sys.argv[1]

second_number = sys.argv[2]

### Problem solving ###

sorted_number_argument = number_sort(first_number, second_number)

list_number_complete = range_min_max(sorted_number_argument)

good_sentence_print = print_correct(list_number_complete)

### Result ###

print(good_sentence_print)