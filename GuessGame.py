import random

guess_game_number = 10


def generate_number(num):
    return random.randint(1, num)


def get_guess_from_user(number):
    user_flag = True
    while user_flag:
        try:
            guess_num = int(input(f"Please guess number from 1 to {number}: \n"))
        except ValueError:
            print("this not a number")
            guess_num = int(input(f"Please guess number from 1 to {number}: \n"))

        if 1 <= guess_num <= number:
            return guess_num


def compare_results(guess_num, secret_number):
    return secret_number == guess_num


def play(difficulty):
    number = difficulty * guess_game_number
    secret_number = generate_number(number)
    user_guess = get_guess_from_user(number)
    condition = compare_results(user_guess, secret_number)
    if condition:
        print("you win in the guess game")
        return True
    else:
        print("you lose in the guess game ")
        return False
