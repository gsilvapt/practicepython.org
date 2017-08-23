#!/usr/bin/env/python3
"""
By gsilvapt
practicepython.org second exercise
"""

def main():
    """
        Function to ask for numbers and check whether it is odd or even.
        (int) -> str
        Second part gets another number and checks if you can divide evenly 
        into the first number.
    """
    num = input("Give me a number to figure out if it is even or odd: ")
    if int(num) % 4 == 0:
        print("Interesting, your number is a multiple of 4.")
    elif int(num) % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")

    check = input("Give me another number: ")
    if int(num) % int(check) == 0:
        print("Your new number divides evenly with the first one!")
    else:
        print("Nice try but your numbers do not evenly divide each other.")

if __name__ == "__main__":
    main()
