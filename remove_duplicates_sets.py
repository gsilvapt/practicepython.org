#!/usr/bin/env/python3
import random

def list_generator(prompt):
    '''
    by: gsilvapt
    Function to generate a random list.
    (prompt) -> (list, int)
    '''
    return random.sample(range(1, 10), random.randint(1, 10))

def cleaned_list(list_a, list_b):
    '''
    Function to clear a list of duplicates. 
    Two lists are generated randomly and returns a new list without duplicates.
    ((list, int), (list, int)) -> (list, int)
    '''
    list_a = list_generator(list_a)
    list_b = list_generator(list_b)
    print('Printing random generated lists: ')
    print(list_a)
    print(list_b)
    list_c = []
    lists = [list_a, list_b]
    for l in lists:
        list_c.extend(l)
    return set(list_c)

if __name__ == "__main__":
    print(cleaned_list(list_generator(input('Click to generate one random list. \
            ')), list_generator(input('Generating another random list. '))))
