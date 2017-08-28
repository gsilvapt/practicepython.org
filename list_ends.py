#!/usr/bin/env/python3
import random

def getList(prompt):
    """
    by: gsilvapt
    Function to get a list from user input or generate a random one.
    (str) -> list, int
    """
    return input(prompt)

def first_and_last(a_list):
    """
    by: gsilvapt
    Function to get the first and last element of a list, either generated 
    randomly or given by user.
    (lst) -> int, int
    """
    a_list = random.sample(range(1, 101), random.randint(1, 101))
    print([a_list[0], a_list[len(a_list)-1]])

if __name__ == "__main__":
    first_and_last(getList('Press any key to generate a random list and' \
            ' find its first and last values. '))
