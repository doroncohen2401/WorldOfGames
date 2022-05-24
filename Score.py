import os.path


# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
def add_score(difficult):
    POINTS_OF_WINNING = difficult * 3 + 5
    print("you add " + str(POINTS_OF_WINNING) + " to your score")
    exists_flag = os.path.exists("scores.txt")
    if exists_flag:
        with open("Scores.txt", "r") as read_file:
            content = read_file.read()
            content = int(content)
        with open("Scores.txt", "w") as write_file:
            write_file.write(str(content + POINTS_OF_WINNING))
    else:
        with open("Scores.txt", "w+") as create_file:
            create_file.write(str(POINTS_OF_WINNING))
