############### Chiffres only ###############

import sys, re

### Function ###

def is_number(arg: any) -> bool:

    for char in arg:

        if not re.match(r"\d", char):
            return False
    
    else:
        return True


def incorrect_argument_count() -> None:

    if len(sys.argv) != 2:
        print("Error")
        exit()


### Error ###

incorrect_argument_count()


### Parsing ###

number_arg = sys.argv[1]

### Problem solving ###

arg_is_numbber = is_number(number_arg)

### Result ###

print(arg_is_numbber)