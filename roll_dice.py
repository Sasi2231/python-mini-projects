import random
while True:
    choice = input('Do you wan to roll the dice? (y/n):').lower()
    if choice == 'y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f'({die1},{die2})')
    elif choice == 'n':
        print('thanks for your time')
        break
    else:
        print('invalid choice')
        continue
    