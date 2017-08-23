#!/usr/bin/env/python3
"""
by: gsilvapt
3rd exercise for practicepython.org
"""
def main():
        """
        Part I:
        Function that, from list a, prints numbers smaller than 5.
        (list int) -> (list int < 5)
        """
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        #for i in a:
        #       if i < 5: 
        #               print(int(i))
        # Ugly solution, brings traceback.
        """
        Part II:
        Ask the user for a given number and print a new list with numbers 
        only smaller than the input.
        """
        num = int(input("Give me a number: "))
        new_list = []   
        for i in a:
                if i < num:
                        new_list.append(i)
        print(new_list)

if __name__ == "__main__":
        main()
