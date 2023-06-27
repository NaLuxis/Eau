############### Suite de Fibonacci ###############

import sys

from typing import List

### Function ###

def addition(a: int, b: int) -> int:

    return a + b


def fibonacci(target: int) -> int:

    sequence = [0, 1]

    if target == 0:
        return 0
    
    for index in range(target - 1):

        sequence.append(addition(sequence[- 2], sequence[ - 1]))

        if target == index:
            break

    return sequence[- 1]


def have_not_correct_number_of_arguments() -> None:

    if len(sys.argv) != 2:
        print(-1)
        exit()


def is_number(target: any) -> bool:

    if not str(target).isdigit():
        return True


def is_negative(target: int) -> bool:

    if int(target) < 0:
        return True


def is_number_too_long(target: int) -> bool:

    if int(target) > 100_000:
        return False


def error_arg(target: int) -> None:

    if is_number(target):
        print(-1)
        exit()

    if is_negative(target):
        print(-1)
        exit()

    if is_number_too_long(target):
        print(-1)
        exit()


### Error ###

have_not_correct_number_of_arguments()

error_arg(sys.argv[1])

### Parsing ###

fibonacci_target = int(sys.argv[1])

### Problem solving ###

result = fibonacci(fibonacci_target)

### Result ###

print(result)