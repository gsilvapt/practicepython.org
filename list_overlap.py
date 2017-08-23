#!/usr/bin/env/python3

def main():
    """
    by: gsilvapt
    Solution for exercise 5 of practicepython.org
    Function to check for equal values in two lists and create another with 
    uniques.
    (list, int), (list, int) -> (list, int)
    """
    # Part I - With pre-defined lists
    list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
    list_c = []
    for i in list_a:
        if i in list_b and i not in list_c:
            list_c.append(i)
    print(list_c)

    # Part II - With random lists with range from 1 to 100 and with numbers
    # from 1 to 100
    import random   # Necessary to generate random lists
    list_d = random.sample(range(1, 101), random.randint(1, 101))
    print('Randomly generated list: \n\n' + str(list_d))
    list_e = random.sample(range(1, 101), random.randint(1, 101))
    print('Randomly generated list: \n\n' + str(list_e))
    list_f = []
    for i in list_e:
        if i in list_d and i not in list_f:
            list_f.append(i)
    print('New list with repeated numbers in lists: \n\n' + str(list_f))
if __name__ == "__main__":
    main()
