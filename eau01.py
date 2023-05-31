############### Combinaisons de 2 nombres ###############

from typing import List

### Function ###

def create_combination() -> List[List[str]]:
    """Combination from 0000 to 9999"""

    combination = []

    for num in range(10000):
        combination.append([f"{num:04}"])
        
    return combination


def format_list(list_combination: List[List[str]]) -> List[List[str]]:
    
    good_format = []

    for num in list_combination:
        for string_number in num:
            first_number = string_number[0:2]
            second_number = string_number[2:4]
            good_format.append([first_number,second_number])

    return good_format


def validate(good_format_combination: List[List[str]]) -> List[List[str]]:
    """Unique combination"""

    valid_combinations = []

    for num in good_format_combination:
        if num[0] <= num[1] and num[0] != num[1]:
            valid_combinations.append(num)

    return valid_combinations


def print_combination(valide_list: List[List[int]]) -> str:
    """Affiche les combinaisons valides correctement"""

    for num in valide_list:
        print(f"{num[0]} {num[1]}", end="")

        if num == valide_list[-1]:
            break
        print("", end=",  ")
    print("")

### Problem solving ###

all_combination = create_combination()

good_format_combination = format_list(all_combination)

valide_combination = validate(good_format_combination)

### Result ###

print_combination(valide_combination)