############### Combinaisons de 3 chiffres ###############

### Import ###

from typing import List

### Function ###

def validate_combinaison(combination: List[int]) -> List[int]:
    """Valide les combinaisonts données de 3 chiffres pour qu'elle soit unique et les 3 chiffres soit dans l'ordre croissant"""

    print(combination)


def create_combination() -> List[int]:
    """A définir"""

    combination = [0, 0, 0]

    for hundreds in range(10):
        combination[0] = hundreds
        for tens in range(10):
            combination[1] = tens
            for units in range(10):
                combination[2] = units
                validate_combinaison(combination)

    


create_combination()






### Error ###




### Parsing ###




### Problem solving ###

def main() -> None:
    """Point d'entrée du programme"""
    



### Result ###


if __name__ == "__main__":
    main()