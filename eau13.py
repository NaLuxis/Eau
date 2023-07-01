############### Tri par sélection ###############

import sys

from typing import List

### Function ###

def select_sort(array_to_select: List[str]) -> List[str]:

    for index in range(0, len(array_to_select) - 1):
        minimum = index

        for step in range(index + 1, len(array_to_select)):
            
            if array_to_select[step] < array_to_select[minimum]:
                minimum = step
            
        if minimum != index:
            array_to_select[index], array_to_select[minimum] = array_to_select[minimum], array_to_select[index]
    
    return array_to_select


def print_correct(select_array: List[str]) -> int:

    for number in select_array:
        print(f"{int(number)} ", end="")
    
    print("")
    exit()

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

list_to_select = sys.argv[1:]

### Problem solving ###

selected_list = select_sort(list_to_select)

correct_sentence = print_correct(selected_list)

### Result ###

print(correct_sentence)