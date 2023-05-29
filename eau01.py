############### Combinaisons de 2 nombres ###############

from typing import List

### Function ###

def create_combination() -> List[List[int]]:
    """Combination from 0000 to 9999"""

    combination_list = []

    for thousands in range(10):    
        for hundreds in range(10):
            for tens in range(10):
                for units in range(10):
                    combination_list.append([thousands, hundreds, tens, units])
    
    return combination_list


def validate_combination(combination_list: List[List[int]]) -> List[int]:
    """Unique and ascending combination"""

    # print(combination_list)
    valid_combinations = []

    for num in combination_list:
        number_1 = num[0:2]
        number_2 = num[2:4]
        print(f"{number_1} {number_2}")

    return valid_combinations


def print_combination(valide_combination_list: List[List[int]]) -> str:
    """Affiche les combinaisons valides correctement"""

    for num in valide_combination_list:
        for chart in num:
            print(f"{chart}", end="")

        if num == valide_combination_list[-1]:
            break
        print(f",", end=" ")   
    print("")


### Problem solving ###

all_combination = create_combination()
all_valide_combination = validate_combination(all_combination)

### Result ###

print_combination(all_valide_combination)