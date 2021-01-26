import random

hangman_pics = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''', '''
   +---+
   |   |
   O   |
 ./|\  |
  / \  |
       |
 =========''', '''
   +---+
   |   |
   O   |
 ./|\. |
  / \  |
       |
 =========''', '''
   +---+
   |   |
   O   |
 ./|\. |
 ./ \  |
       |
 =========''', '''
   +---+
   |   |
   O   |
 ./|\. |
 ./ \. |
       |
 =========''']
 pic = 0
 # Opens and copies the text of a book's .txt file
 with open('https://github.com/PdxCodeGuild/class_platypus/blob/master/Code/Mitchell/english.txt', 'r') as f:
     input_text = f.read()

         board = board + '_ '
     # Loop until they player runs out of guesses
     while guesses > 0:
         print(hangman_pics[pic])
         print(board)
         print('# of guesses remaining: ' + str(guesses))
         print('already guessed: ' + already_guessed)

             if picked.find(letter_guess) == -1:
                 already_guessed = already_guessed + letter_guess + ', '
                 guesses -= 1
                 pic += 1
                 break
     # Prints win/lose message and play again option
     if won == True:
         print('You won!')
     else:
         print(hangman_pics[10])
         print('You lost...')
     play_again = input('Do you want to play again? (type "yes" or "no") ').lower()
     if play_again == 'no':
         playing = False
