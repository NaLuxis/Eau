############### Différence minimum absolue ###############

import sys

from typing import List

### Function ###

def number_sort(list_to_sort: List[str]) -> List[int]:

    new_list = []

    for element in list_to_sort:
        new_list.append(int(element))

    sorted_list = sorted(new_list)

    return sorted_list


def calculation_absolute_difference(min_number: int, max_number: int) -> int:

    return max_number - min_number


def calculation_minimum_absolute_difference(list_to_find: List[int]) -> int:

    min_absolute_difference = float("inf")

    for index in range(0, len(list_to_find) - 1):

        number_one = list_to_find[index]
        number_two = list_to_find[index + 1]

        pair_list = [number_one, number_two]
        
        diff = calculation_absolute_difference(pair_list[0], pair_list[1])

        if diff < min_absolute_difference:
            min_absolute_difference = diff

    return min_absolute_difference


def incorrect_argument_count() -> None:

    if len(sys.argv) <= 2:
        print("Error")
        exit()


def is_number(target: any) -> bool:

    if str(target).lstrip("+-").isdigit():
        return True


def error_argument() -> None:

    for element in sys.argv[1:]:

        if is_number(element):
            pass
        else:
            print("Error")
            exit()
    

### Error ###

incorrect_argument_count()

error_argument()

### Parsing ###

number_list = sys.argv[1:]

### Problem solving ###

sorted_list = number_sort(number_list)

minimum_absolute_difference = calculation_minimum_absolute_difference(sorted_list)

### Result ###

print(minimum_absolute_difference)