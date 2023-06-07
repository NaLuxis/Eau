############### Prochain nombre premier ###############

import sys

from typing import List

### Function ###

def is_prime_number(target: int) -> bool:

    for num in range(2,int(target ** 0.5) + 1):

        if target % num == 0 and num != target:
            return False
        
        if num == target:
            return True


def give_all_prime_number(target: int) -> int:
    
    prime_number_list = []
        
    for num in range(target + 1):

        if is_prime_number(num):
            prime_number_list.append(num)

    return prime_number_list[-1]


def add_one_prime_number(target: int) -> int:

    count = target

    for num in range(count, count + 10_000):

        if is_prime_number(num):
            return num
        
        count =+ 1

        print(count)

print(add_one_prime_number(10))

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

all_prime_number = give_all_prime_number(target_prime_number)

next_prime_number = add_one_prime_number(all_prime_number)

### Result ###

# print(next_prime_number)