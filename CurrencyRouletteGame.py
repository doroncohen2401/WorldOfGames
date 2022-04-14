import requests
from GuessGame import generate_number


class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

            # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


def gen_currency_rate(num):
    url_api = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url_api)
    currency = converter.convert('USD', 'ILS', num)
    return currency


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
    current_exchange_rate = gen_currency_rate(random_number)
    money_range = get_money_interval(current_exchange_rate, difficult)
    guess_number = get_guess_from_user(random_number)
    condition = money_range[0] <= guess_number <= money_range[1]
    if condition:
        print("you win in the guess game")
        return True
    else:
        print("you lose in the guess game ")
        return False
