import MemoryGame as MG
import GuessGame as GG
import CurrencyRouletteGame as CRG
import Score


def welcome(name):
    return f"""Hello {name} and welcome to the World Of Games (WOG).
Here you can find many cool games to play."""


def choose_game():
    game_flag = True
    while game_flag:
        try:
            game_number = int(input("""Please choose a game to play: 
             1. Memory Game - a sequence of numbers will appear for 1 second and you have to
                guess it back 
             2. Guess Game - guess a number and see if you chose like the computer
             3. Currency Roulette - try and guess the value of a random amount of USD in ILS
                 """))
        except:
            print("this not  number")
        if 1 <= game_number <= 3:
            return game_number
        else:
            print("this not valid choose")


def choose_difficult():
    difficult_flag = True
    while difficult_flag:
        try:
            difficult_num = int(input("Please choose game difficulty from 1 to 5: "))
        except:
            print("this not  number")
        if 1 <= difficult_num <= 5:
            return difficult_num
        else:
            print("this not valid choose")


def load_game():
    game_number = choose_game()
    difficult = choose_difficult()
    if game_number == 1:
        win = MG.play(difficult)
    elif game_number == 2:
        win = GG.play(difficult)
    elif game_number == 3:
        win = CRG.play(difficult)

    if win:
        Score.add_score(difficult)
