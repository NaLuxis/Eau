############### Majuscule ###############

import sys, re

### Function ###

def capitalize_first_letter(arg: str) -> str:
    ...


def incorrect_argument_count() -> None:

    if len(sys.argv) != 2:
        print("Error")
        exit()


def has_no_letters(a: str) -> bool:
    
    if re.search(r"[a-zA-Z]+", a):
        return True


def error_argument(a: str) -> None:

    if has_no_letters(a):
        pass
    else:
        print("Error")
        exit()


### Error ###

incorrect_argument_count()

error_argument(sys.argv[1])

### Parsing ###




### Problem solving ###




### Result ###