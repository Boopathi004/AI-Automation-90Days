# genrating random password 
import string
import random

lettres=string.ascii_letters
numbers=string.digits
symbles="!@#$%^&*"

all_lettres=lettres+numbers+symbles
password=""
print("Genrate a passowrd ")

for i in range(12):
    password+=random.choice(all_lettres)
    print(password)