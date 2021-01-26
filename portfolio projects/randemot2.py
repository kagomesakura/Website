#import random


#eyes = [':',';','=']
#nose = ['^','~','-']
#mouth = [')','(','p','x','/','O','D']

#print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))


import random


def create_emoticon():

    list_eyes = [':', '=', ';']
    list_noses = ['', '-', '\'', '^', '+']
    list_mouths = [')', ']', '|', '/', '\\', 'D', 'P', '3']

    eyes = random.choice(list_eyes)
    nose = random.choice(list_noses)
    mouth = random.choice(list_mouths)

    emoticon = eyes + nose + mouth

    return emoticon


for i in range(5):
    print(create_emoticon())
