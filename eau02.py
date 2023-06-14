############### Paramètres à l’envers ###############

import sys

from typing import List

### Function ###

def inverse_list(arguments_list: List[str]) -> List[str]:
    
    return arguments_list[::-1]

def is_correct_argument_length(arguments_list: List[str] = sys.argv) -> None:

    if len(arguments_list) < 2:
        print("Erreur, aucun arguments donnés")
        exit()

def print_arguments(list_element: List[str]) -> None:

    for elements in list_element:
        print(elements)


### Error ###

is_correct_argument_length()

### Parsing ###

list_arguments = sys.argv[1:]

### Problem solving ###

inversed_list = inverse_list(list_arguments)

### Result ###

print_arguments(inversed_list)