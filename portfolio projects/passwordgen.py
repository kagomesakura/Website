import random
import string

a_num = input('How many letters in your password? ')
a_num = int(a_num)
chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
out_string = ''
for i in range(0, a_num):
    out_string = out_string + random.choice(chars)

print(out_string)
