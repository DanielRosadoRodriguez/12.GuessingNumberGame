# import random library to use the function random.choice
import random


def pick_number():
    """
    Function that picks a random number between 1 - 100
    :return: random_number
    """
    random_number = random.choice(range(1, 101))
    return random_number
