def get_user_guess():
    """
    function that receives the user guess
    validates that the entry is an integer
    transforms the entry into an integer
    :return: guess
    """
    # asks for the number until the user enters an integer
    while True:
        try:
            guess = int(input("Insert your guess: \n"))
        except ValueError:
            print("Enter a valid whole number")
            continue
        else:
            return guess


def game_core(lives, machine_number):
    """
    main game functionality
    checks if the number is equal to the one chosen by the machine
    if it is, the user wins
    if isn't the user loses one live
    if the lives reach 0, the user loses the game
    :param machine_number:
    :param lives:
    :return:None
    """

    while True:
        if lives > 0:
            user_guess = get_user_guess()
            if user_guess == machine_number:
                print("You Win!")
                break
            else:
                lives -= 1
                if user_guess > machine_number:
                    print("Too High!")
                elif user_guess < machine_number:
                    print("Too Low!")
                print(f"You have {lives} remaining")
        else:
            print("You Lose")
            break
