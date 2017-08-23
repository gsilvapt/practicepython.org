#!/usr/bin/env/python3
def isPalindrome():
    """
    by: gsilvapt
    Function to find if an input string is a palindrome.
    (str) -> str
    """
    word = input("Give me a word and I'll tell if it is a palindrome: ")
    if str(word) == str(word)[::-1]:	# Checks if strings matches its reverse
        print ("Great!, the world is a palindrome.")
    else:
        print ("Sorry, the word is not a palindrome.")

if __name__ == "__main__":
    isPalindrome()
