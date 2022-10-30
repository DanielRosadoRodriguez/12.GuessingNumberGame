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
