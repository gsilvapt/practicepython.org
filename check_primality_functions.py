#!/usr/bin/env/python3
"""
by: gsilvapt
Function to find if a number is a prime or not,
(int) -> str, int
"""
def fetch_number(prompt):
    """
    Asks for a number to see if it is prime.
    (str) -> int
    """
    return int(input(prompt))

def is_prime(number):
    """
    Computes if number from prompt is prime. True for prime, False otherwise.
    While doing the math, it is important to round the final result to avoid
    TypeError.
    (int) -> bool
    """
    if number == 1:
        prime = False 
    elif number == 2:
        prime = True
    else:
        prime = True
        for i in range(2, round(number/2)+1):  # This round()
            if number % i == 0:
                prime = False
                break
    return prime

def do_print(number):
    """
    Prints results based on previous results.
    (bool) -> str
    prime = is_prime(number)
    """
    prime = is_prime(number)
    if prime:
        print('Your number ' + str(number) + ' is prime. ')
    else: 
        print('Your number ' + str(number) + ' is not prime.')

while 1 == 1:
    """
    Basic infinite loop to repeat until user presses ctrl-c
    """
    do_print(fetch_number('Give me a number to check if it is prime:' \
            ' (ctrl-c to exit) '))
