# import requests
from currency_converter import CurrencyConverter
from GuessGame import generate_number


def gen_currency_converter(from_currency, to_currency, amount):
    c = CurrencyConverter()
    return c.convert(amount, from_currency, to_currency)


def get_money_interval(total, difficult):
    return total - (5 - difficult), total + (5 - difficult)


def get_guess_from_user(usa_dollar):
    user_flag = True
    while user_flag:
        try:
            guess_num = float(input(f"How many shekels do you think are worth the {usa_dollar} USD? : \n"))
        except ValueError:
            print("this not a number")

        if type(guess_num) == float:
            return guess_num


def play(difficult):
    random_number = generate_number(101)
    currency_converter = gen_currency_converter("USD", "ILS", float(random_number))
    money_range = get_money_interval(currency_converter, difficult)
    guess_number = get_guess_from_user(random_number)
    condition = money_range[0] <= guess_number <= money_range[1]
    if condition:
        print("you win in the guess game")
        return True
    else:
        print("you lose in the guess game ")
        return False
