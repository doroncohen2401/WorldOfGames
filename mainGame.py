from Live import load_game, welcome

print(welcome("doron"))
flagGame = True

while flagGame:
    load_game()
    exitGame = input("if you want to quit press q or Q")
    if exitGame == "q" or exitGame == "Q":
        flagGame = False


