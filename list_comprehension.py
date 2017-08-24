#!/usr/bin/env/python3

def isEven():
    """
    by: gsilvapt
    Function to find and return even numbers in a random list.
    (list, int) -> (list, int)
    """
    import random
    # Random list from 1 to 1001, with random range from 1 to 1001
    list = random.sample(range(1,1001), random.randint(1,1001))
    evens = [element for element in list if element % 2 == 0]
    print(evens)

if __name__ == "__main__":
    isEven()
