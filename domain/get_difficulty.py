def get_difficulty():
    """
    function that allows the user to input the level of difficulty that wants for the game
    validates the entry until the user inputs a valid option
    :return: lives
    """
    while True:
        difficulty = input("Insert which difficulty level you want: easy or hard?\n").lower()
        if difficulty == "easy":
            lives = 10
            break
        elif difficulty == "hard":
            lives = 5
            break
        else:
            print(f"'{difficulty}' is not a valid level, the valid levels are 'easy' or 'hard'")

    return lives
