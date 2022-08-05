import random
you = input("Choose either 'R','P', or 'S': ")
def rock_paper_scissors_game(comp_selection, you):
    if comp_selection == you:
        print('Match Drawn')
    if comp_selection == 'R' and you == 'P':
        print("You Won!")
    elif comp_selection == 'P' and you == 'R':
        print('You Lose!')
    elif comp_selection == 'S' and you == 'R':
        print('You Won!')
    elif comp_selection == 'R' and you == 'S':
        print('You Lose!')
    elif comp_selection == 'P' and you == 'S':
        print('You Won!')
    elif comp_selection == 'S' and you == 'P':
        print('You Lose!')
    elif you == '':
        print('You must choose the initial to start the game!')
    elif you == 's' or you =='r' or you == 'p':
        print("You must choose Capital letter's initial to start the game!!!")
    else:
        print('You must choose correct initials')



comp_number = random.randint(1,3)
# print(comp_number)
if comp_number == 1:
    comp_selection = 'R'
elif comp_number == 2:
    comp_selection = 'P'
else:
    comp_selection = 'S'
print(f"You chose {you} and the Computer chose {comp_selection}.")
rock_paper_scissors_game(comp_selection,you)
