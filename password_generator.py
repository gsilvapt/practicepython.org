#!/usr/bin/python3 
import random

"""
by: gsilvapt
Python script to generator a password according to user input
(int, str) -> str
"""
def weak_password():
    random.seed(random.choice(Words))
    Password = list(random.choice(Words))
    Password[random.randint(0,7)]=str(random.randint(0, 99))
    return "".join(Password)

def average_password(length):
    random.seed(random.choice(Words))
    random.shuffle(Avg)
    Password = [random.choice(Avg) for i in range(int(length))]
    return "".join(Password)

def strong_password(length):
    random.seed(random.choice(Words))
    random.shuffle(AllWords)
    Password = [random.choice(AllWords) for i in range(int(length))]
    return "".join(Password)

Words = ['actually', 'expected', 'computers', 'adiction', 'sports', 
        'provided', 'american', 'business', 'economics', 'deviation',
        'organizations', 'open source', 'python', 'programming', 'java',
        'nephew', 'thinking', 'solving', 'macOS', 'The Mole', 'programs',
        ]

AllWords= list("!)*+,-./0123456789:;<=>DEF?@ABCGHI#$%&\(JKLMNOPQRSTUVWXYZabcdef\
        ghijklmnopqrstuvwxyz")

Avg = list("ahijklbcd0123456789efgmnopqrstuvwxyz0123456789")


while True:
    UserInput = input('How strong should the password be? (weak - w, '\
            'average - a, strong- s)? ')
    if UserInput == "w":
        print("New password is: " + weak_password())
        break
    elif UserInput == "a":
        length = input('How long should the password be? ')
        print("New password is: " + average_password(length))
        break
    elif UserInput == "s":
        length = input('How long should the password be? ')
        print("New password is: " + strong_password(length))
        break
    else:
        break
