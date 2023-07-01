############### Index wanted ###############

import sys

from typing import List

### Function ###

def search_index(list_to_search: List[any], element_to_find: any) -> int:

    count = 0

    for element in list_to_search:

        if element == list_to_search[-1] and element_to_find != element:
            return -1

        if element_to_find == element:
            return count
        
        count += 1


def incorrect_argument_count() -> None:

    if len(sys.argv) <= 2:
        print("Error")
        exit()


### Error ###

incorrect_argument_count()

### Parsing ###

search_list = sys.argv[1:-1]

search_element = sys.argv[-1]

### Problem solving ###

index_wanted = search_index(search_list, search_element)

### Result ###

print(index_wanted)