#!/usr/bin/env/python3
def duplicatesWithOverlap():
    """
    by: gsilvapt
    Function to find duplicates in two lists using list overlap method.
    Lists are generated randomly again.
    (list, int) -> list, int
    """
    import random
    a = random.sample(range(1,1001), random.randint(1,1001))
    b = random.sample(range(1,1001), random.randint(1,1001))
    duplicates = [i for i in a if i in b]
    print(duplicates)
if __name__ == "__main__":
    duplicatesWithOverlap()
