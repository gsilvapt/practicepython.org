#!/usr/bin/env/python3

def get_intervals(prompt):
    '''
    by: gsilvapt
    Function to retrieve information on the number of fibonacci numbers user
    wants to generate.
    ex: How many fibonacci numbers you want to generate.
    sequence.
    (int) -> list, int
    '''
    return input(prompt)

def fib_seq(numbers):
    '''
    Function to compute fibonacci numbers.
    (int) -> int
    '''
    fib = []
    i = 1
    if int(numbers) == 0:
        fib = []
    if int(numbers) == 1:
        fib = [1]
    if int(numbers) == 2:
        fib = [1, 1]
    elif int(numbers) > 2:
        fib = [1, 1]
        while i < (int(numbers)- i):
            fib.append(fib[i] + fib[i-1])
            i += 1
    print(fib)

if __name__ == "__main__":
    fib_seq(get_intervals('How many fibonacci numbers do you wish to '\
            'generate? '))
