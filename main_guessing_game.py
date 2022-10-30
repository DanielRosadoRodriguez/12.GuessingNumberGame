# imports
from domain import print_wellcome as pw
from domain import pick_number as pn
from domain import get_difficulty as gd
from domain import get_user_guess as gug


# print the wellcome to the user
pw.print_wellcome()
# generate the random number the user will guess
number = pn.pick_number()

# lets the user pick a difficulty level and sets the user lives for the game
user_lives = gd.get_difficulty()
print(f"You have {user_lives} lives!")


while True:
    user_guess = gug.get_user_guess()
    if user_guess == number:
        print("You Win!")
        break
    else:
        if user_lives > 0:
            user_lives -= 1
            print(f"You have {user_lives} remaining")
        else:
            print("You Lose")
            break

