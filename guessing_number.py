import random
number_to_guess = random.randint(1,100)
while True:
    try:
        guess = int(input('guess the number between 1 to 100:'))
        if guess > number_to_guess:
            print('Too high!')
        elif guess < number_to_guess:
            print('Too low!')
        else:
            print('congratulations! you guessed it right')
            break
    except:
        print('please enter valid number')