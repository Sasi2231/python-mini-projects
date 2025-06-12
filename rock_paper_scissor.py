# Ask user to make choice
# if input is invalid 
 # print error
# let computer make the choice 
# print the results 
# anounce winner
# if he wants to continue continue
# else terminate
import random
emojis = {'r':'🪨','p':'📃','s':'✂️'}
choices=('r','p','s')
user_choice =input('Rock, paper or scissors? (r/p/s):')
if user_choice not in choices:
    print('Enter valid input')
computer_choice = random.choice(choices)
print(f'you chose {emojis[user_choice]}')
print(f'computer chose {emojis[computer_choice]}')
if user_choice == computer_choice:
    print('Tie!')
elif (
    (user_choice == 'r' and computer_choice =='s') or
    (user_choice == 'p' and computer_choice == 'r') or
    (user_choice == 's' and computer_choice == 'p')
):
    print('you win!')
else:
    print('you lose!')