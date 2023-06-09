############### Prochain nombre premier ###############

import sys

from typing import List

### Function ###

def is_prime_number(target: int) -> bool:

    if target <= 1:
        return False
    
    if target == 2:
        return True
    
    if target % 2 == 0:
        return False
    else:
        for num in range(3, int(target ** 0.5) + 1, 2):

            if target % num == 0:
                return False
            
    return True


def give_all_prime_number(target: int) -> int:
    
    prime_number_list = []
        
    for num in range(target + 1):

        if is_prime_number(num):
            prime_number_list.append(num)

    return prime_number_list[-1]


def add_one_prime_number(target: int) -> int:

    target += 1

    while not is_prime_number(target):

        target += 1
    
    return target
        

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


def error_arg(target: int) -> None:

    if is_number(target):
        print(-1)
        exit()

    if is_negative(target):
        print(-1)
        exit()


### Error ###

have_not_correct_number_of_arguments()

error_arg(sys.argv[1])

### Parsing ###

target_prime_number = int(sys.argv[1])

### Problem solving ###

last_prime_number = give_all_prime_number(target_prime_number)

next_prime_number = add_one_prime_number(last_prime_number)

### Result ###

print(next_prime_number)