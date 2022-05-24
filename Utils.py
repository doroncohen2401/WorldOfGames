import os
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = "OC4"
# The screen clear function
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')
