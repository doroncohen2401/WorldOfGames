import os
from time import sleep
from numpy import array_equal
from GuessGame import generate_number

size_list = 2
range_numbers = 101


# The screen clear function
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


def generate_sequence(difficulty):
    list_num = []
    for i in range(difficulty * size_list):
        list_num.append(generate_number(range_numbers))
    return list_num


def get_list_from_user():
    user_flag = True
    while user_flag:
        try:
            # convert from string to int arr
            memory_list = list(map(int, (input(f"Please write what you remember : \n")).split()))
        except ValueError:
            print("only numbers please")
            # convert from string to int arr
            continue
        return memory_list


def is_list_equal(arr1, arr2):
    return array_equal(arr1, arr2)


def play(difficulty):
    list_generate = generate_sequence(difficulty)
    print(list_generate)
    sleep(0.7)
    screen_clear()
    print('\n' * 80)
    condition = is_list_equal(list_generate, get_list_from_user())
    if condition:
        print("you win in the guess game")
        return True
    else:
        print("you lose in the guess game ")
        return False
