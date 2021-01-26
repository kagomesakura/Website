import random
import string


chars = string.ascii_lowercase + string.digits + string.ascii_uppercase

password = ''
for i in range(10):
    password = password + random.choice(chars)

print(password)
