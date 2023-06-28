############### Majuscule ###############

import sys, re

### Function ###

def capitalize_first_letter(arg: str) -> str:

    lower_arg = arg.lower()

    words_list = lower_arg.split(" ")

    final_list = []

    for word in words_list:
        new_word = []
        capitalized_letter = word[0].upper()
        new_word.append(capitalized_letter)
        new_word.append(word[1:])
        final_word = "".join(new_word)
        final_list.append(final_word)

    final_sentence = " ".join(final_list)
    
    return final_sentence



def incorrect_argument_count() -> None:

    if len(sys.argv) != 2:
        print("Error")
        exit()


def has_no_letters(arg: str) -> bool:
    
    if re.search(r"[a-zA-Z]+", arg):
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

string_arg = sys.argv[1]

### Problem solving ###

capitalize = capitalize_first_letter(string_arg)

### Result ###

print(capitalize)