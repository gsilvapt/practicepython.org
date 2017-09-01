#!/usr/bin/env/python3
import random

def list_generator(prompt):
    '''
    Function to generate a random list.
    (prompt) -> (list, int)
    '''
    return random.sample(range(1, 51), random.randint(1, 51))

def cleaned_list(list_a, list_b):
    '''
    by: gsilvapt
    Function to clear a list of duplicates. 
    Two lists are generated randomly and returns a new list without duplicates.
    ((list, int), (list, int)) -> (list, int)
    '''
    list_a = list_generator(list_a)
    list_b = list_generator(list_b)
    print(list_a)
    print('\n')
    print(list_b)
    list_c = []
    for i in list_a:
        if int(i) in list_b and int(i) not in list_c:
            list_c.append(i)
    if not list_c: 
        print('There are no duplicates. ')
    else:
        print(list_c)

if __name__ == "__main__":
    cleaned_list(list_generator(input('Click to generate one random list. \
            ')), list_generator(input('Generating another random list. '))) 
