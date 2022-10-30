# imports
from domain import print_wellcome as pw
from domain import pick_number as pn
from domain import get_difficulty as gd
from domain import game_core as gc

# print the wellcome to the user
pw.print_wellcome()


while True:
    # generate the random number the user will guess
    number = pn.pick_number()

    # lets the user pick a difficulty level and sets the user lives for the game
    user_lives = gd.get_difficulty()
    print(f"You have {user_lives} lives!")
    gc.game_core(lives=user_lives, machine_number=number)
    play_again = input("Do you want to play again? y/n\n").lower()
    if play_again != "y":
        print("See you soon!")
        break
