#!/usr/bin/env/python3

def get_long_string(prompt):
    '''
    by: gsilvapt
    Requests long string to user.
    (prompt) -> str
    '''
    return input(prompt)

def reverser(words):
    Words = get_long_string(words)
    WordList = words.split()
    WordList.reverse()
    return " ".join(WordList)

if __name__ == "__main__":
    print(reverser(get_long_string('Introduce a long string, like a paragraph' \
            ' of text. ')))
