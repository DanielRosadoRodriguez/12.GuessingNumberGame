from domain import print_wellcome as pw
from domain import pick_number as pn
from domain import get_difficulty as gd


pw.print_wellcome()
number = pn.pick_number()

user_lives = gd.get_difficulty()
print(f"You have {user_lives} lives!")
