from domain import print_wellcome as pw
from domain import pick_number as pn

pw.print_wellcome()
number = pn.pick_number()

while True:
    difficulty = input("Insert which difficulty level you want: easy or hard?\n")
    if difficulty == "easy":
        lives = 10
        break
    elif difficulty == "hard":
        lives = 5
        break
    else:
        print(f"'{difficulty}' is not a valid level, the valid levels are 'easy' or 'hard'")

print(f"You have {lives} lives!")
