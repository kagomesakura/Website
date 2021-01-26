import random
import os
from colorama import Fore, Back, Style

''' Train engineers don't like cows in the way of their tracks, so what else can they do?...
Run them over!'''

def print_ascii_art(cowlogo):
    with open(cowlogo + '.txt', 'r') as f:
        print(f.read())
print(Fore.RED + Back.LIGHTBLACK_EX +Style.NORMAL)
print_ascii_art('cowlogo2')
print(Fore.WHITE + Back.LIGHTBLACK_EX +Style.NORMAL)
print_ascii_art('cowart')

print(Fore.RED + Back.LIGHTBLACK_EX +Style.NORMAL)
os.system("afplay train.mp3")

def get_file(location):
    with open(location + '.txt', 'r') as in_file:
        return in_file

class Lifeform:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cow(Lifeform):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.art = "🐄"

    def moo(self):
        os.system("afplay cow.mp3")

    def move(self):
        x_shift = random.randint(-1, 1)
        y_shift = random.randint(-1, 1)
        if self.x + x_shift in range(20):
            self.x = x_shift + self.x
        if self.y + y_shift in range(20):
            self.y = y_shift + self.y

class Player(Lifeform):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.art = "🚂"
        self.kills = 0

class Board:
    def __init__(self):
#        self.art = " "
        self.width = 20
        self.height = 20


    def board_locations(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def __getitem__(self, train):
        return self.board_locations()

    def print(self, entities):
        print(Fore.RED + Back.LIGHTBLACK_EX + Style.NORMAL)
        for i in range(self.height):
            for j in range(self.width):
                for k in range(len(entities)):
                    if entities[k].y == i and entities[k].x == j:
                        print(entities[k].art + '  ', end='')
                        break
                else:
                    print('.   ', end='')
            print()

theplayer = Player(10, 10)
cow = Cow(random.randint(0,19),random.randint(0,19))


board = Board()
board.print([theplayer, cow])

while True:
    print(Fore.WHITE + Back.LIGHTBLACK_EX + Style.NORMAL)
    cow.move()
    print(f'Cow death count... {theplayer.kills}!')
    command = input('What direction would you like to go?  Left (l), right (r), up (u), or down (d)? \n').lower()


    if command in ['l', 'left', '\x1b[D']:
        theplayer.x -= 1

    elif command in ['r', 'right', '\x1b[C']:
        theplayer.x += 1

    elif command in ['u', 'up', '\x1b[A']:
        theplayer.y -= 1

    elif command in ['d', 'down', '\x1b[B']:
        theplayer.y += 1
    elif command == 'done':
        break
    board.print([theplayer, cow])
    if cow.x == theplayer.x and cow.y == theplayer.y:
        print('You killed the cow! ')
        os.system("afplay cow.mp3")
        cow.x = random.randint(0, 19)
        cow.y = random.randint(0, 19)
        theplayer.kills += 1
