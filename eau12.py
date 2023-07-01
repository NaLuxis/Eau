############### Tri à bulle ###############

import sys

from typing import List

### Function ###

def bubble_sort_opti(array_to_bubble: List[str]) -> List[str]:
    
    for index in range(len(array_to_bubble), 0, -1):

        array_is_sort = True

        for step in range(0, index - 1):

            if array_to_bubble[step + 1] < array_to_bubble[step]:

                array_to_bubble[step + 1], array_to_bubble[step] = array_to_bubble[step], array_to_bubble[step + 1]

                array_is_sort = False
            
        if array_is_sort:
            break
    
    return array_to_bubble


def print_correct(bubble_array: List[str]) -> int:

    for number in bubble_array:
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

list_to_bubble = sys.argv[1:]

### Problem solving ###

bubbled_list = bubble_sort_opti(list_to_bubble)

correct_sentence = print_correct(bubbled_list)

### Result ###

print(correct_sentence)