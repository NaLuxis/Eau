############### Combinaisons de 3 chiffres ###############

### Import ###

from typing import List

### Function ###

def create_combination() -> List[List[int]]:
    """Crée une liste de liste d'integer de 000 à 999"""

    combination = []

    for hundreds in range(10):
        for tens in range(10):
            for units in range(10):
                combination.append([hundreds, tens, units])
    
    return combination


def validate_combination(combination: List[List[int]]) -> List[int]:
    """Valide une combinaisont donnée de 3 chiffres pour qu'elle soit unique et dans l'ordre croissant"""

    valid_combinations = []

    for num in combination:
        if num[0] < num[1] < num[2]:
            valid_combinations.append(num)

    return valid_combinations


def print_combination(valide_combination: List[List[int]]) -> str:
    """Affiche les combinaisons valides correctement"""

    for num in valide_combination:
        for chart in num:
            print(f"{chart}", end="")
        print(f",", end=" ")
    print("")


### Problem solving ###    
### Result ###

result = print_combination(validate_combination(create_combination()))



