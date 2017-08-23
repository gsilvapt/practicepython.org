#!/usr/bin/env/python3
def main():
    """
    by: gsilvapt
    Solution for exercise 4.
    Function to ask for a number and find all its divisors.
    """
    num = int(input("Give me a number and I'll print all its divisors: "))
    for i in range(1,num+1):
        if num % i == 0:
            print(int(i))

if __name__ == "__main__":
    main()
