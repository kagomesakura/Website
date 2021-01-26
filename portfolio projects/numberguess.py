import random

num1 = random.randint(1, 10)
lastguess = None
numguess = 0

def distance(lastguess, guess):
    return abs(lastguess - guess)


while True:
    guess = input('Guess a number between 1 and 10! ')
    guess = int(guess)

    if guess > num1:
        print('You guessed too high!')
    if guess < num1:
        print('You guessed too low.')

    elif guess == num1:
        print('You guessed correctly!')
        break

if lastguess is not None:
    distance = distance(target, guess)
    lastguess = distance(target, lastguess)
    if distance < lastguess:
        print('You\'re getting closer.')
    if distance > lastguess:
        print('You\'re getting warmer!')
    if distance == lastguess:
        print('You\'re in the same spot.')





# distance = abs(current_guess-target) - abs(last_guess-target)
# if distance > num1:
#     print('Cold')
# else:
#     print('Hot!')
