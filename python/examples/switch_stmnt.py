# 1. Using if-elif-else Statements:

def switch_example(value):
    if value == 'a':
        return "You chose option A."
    elif value == 'b':
        return "You chose option B."
    elif value == 'c':
        return "You chose option C."
    else:
        return "Invalid option."


print(switch_example('b'))


# 2. Using Dictionaries for Function Dispatching:

def option_a():
    return "You chose option A."


def option_b():
    return "You chose option B."


def option_c():
    return "You chose option C."


def default():
    return "Invalid option."


switch_dict = {
    'a': option_a,
    'b': option_b,
    'c': option_c
}


def switch_example(value):
    # The `.get()` method returns the default function if the key is not found
    return switch_dict.get(value, default)()


print(switch_example('b'))


# 3. Using match-case (Introduced in Python 3.10):
'''
Starting with Python 3.10, a new match-case statement was introduced, which is similar to the traditional switch-case 
found in other languages.
'''


def switch_example(value):
    match value:
        case 'a':
            return "You chose option A."
        case 'b':
            return "You chose option B."
        case 'c':
            return "You chose option C."
        case _:
            return "Invalid option."


print(switch_example('b'))
