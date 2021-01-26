import random

rps_list = ['rock', 'paper', 'scissors']
while True:
    player = input("rock, paper, scissors? ")
    computer = random.choice(rps_list)

    if player == "rock":
        if computer == "paper":
            print("You Win!")
    if player == "rock":
        if computer == "scissors":
            print("You Win!")
    if player == "paper":
        if computer == "rock":
            print("You lose!")
    if player == "paper":
        if computer == "scissors":
            print("You lose!")
    if player == "scissors":
        if computer == "rock":
            print("You lose!")
    if player == "scissors":
        if computer == "paper":
            print("You win!")
    else:
        print("Tie!")



    play_again = input("Play again yes(y) or no(n)")
    if play_again == 'y':
        print(player)

    if play_again == 'n':
        break
