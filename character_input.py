"""
By: gsilvapt
Exercise for practicepython.org
"""

def main():
    """
    Function gets name and age input;
    Calculates which year the person will be 100 years old
    (str, str) --> (str, int)
    The second part, asks for a number and repeats the name for the same
    number provided.
    """
    name = input("What's your name? ")
    age = input("How old are you? ")
    date = (100-int(age))+2017 
    print (name + ", you will be 100 years old in " + str(date))
    
    number = input("Now, from 1-10, give me a number: ")
    for i in range(int(number)):
        print(name + '\n')
if __name__ == "__main__":
    main()
