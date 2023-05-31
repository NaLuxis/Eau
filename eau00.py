############### Combinaisons de 3 chiffres ###############

from typing import List

### Function ###

def create_combination() -> List[List[int]]:
    """Combination from 000 to 999"""

    combination_list = []

    for hundreds in range(10):
        for tens in range(10):
            for units in range(10):
                combination_list.append([hundreds, tens, units])
    
    return combination_list


def validate(combination_list: List[List[int]]) -> List[int]:
    """Unique and ascending combination"""

    valid_combinations = []

    for num in combination_list:
        if num[0] < num[1] < num[2]:
            valid_combinations.append(num)

    return valid_combinations


def print_result(valide_combination_list: List[List[int]]) -> str:
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
all_valide_combination = validate(all_combination)

### Result ###

print_result(all_valide_combination)