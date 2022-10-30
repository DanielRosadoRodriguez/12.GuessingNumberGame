game_logo = '''

  .-')                _   .-')       ('-.             .-') _             _   .-')   .-. .-')    ('-.  _  .-')    .-')    
 ( OO ).             ( '.( OO )_   _(  OO)           ( OO ) )           ( '.( OO )_ \  ( OO ) _(  OO)( \( -O )  ( OO ).  
(_)---\_) .-'),-----. ,--.   ,--.)(,------.      ,--./ ,--,' ,--. ,--.   ,--.   ,--.);-----.\(,------.,------. (_)---\_) 
/    _ | ( OO'  .-.  '|   `.'   |  |  .---'      |   \ |  |\ |  | |  |   |   `.'   | | .-.  | |  .---'|   /`. '/    _ |  
\  :` `. /   |  | |  ||         |  |  |          |    \|  | )|  | | .-') |         | | '-' /_)|  |    |  /  | |\  :` `.  
 '..`''.)\_) |  |\|  ||  |'.'|  | (|  '--.       |  .     |/ |  |_|( OO )|  |'.'|  | | .-. `.(|  '--. |  |_.' | '..`''.) 
.-._)   \  \ |  | |  ||  |   |  |  |  .--'       |  |\    |  |  | | `-' /|  |   |  | | |  \  ||  .--' |  .  '.'.-._)   \ 
\       /   `'  '-'  '|  |   |  |  |  `---.      |  | \   | ('  '-'(_.-' |  |   |  | | '--'  /|  `---.|  |\  \ \       / 
 `-----'      `-----' `--'   `--'  `------'      `--'  `--'   `-----'    `--'   `--' `------' `------'`--' '--' `-----'  

'''


def print_wellcome():
    """
    Function that prints the wellcome to the program
    """
    print(game_logo)
    print("Wellcome to Number Guessing game")
    print("The machine will pick a random number between 1 - 100 and you have to guess the number")
    print("You can choose between 2 levels of difficulty: ")
    print("     - Easy: 5 lives")
    print("     - Hard: 10 lives")
