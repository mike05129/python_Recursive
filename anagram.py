"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm
from collections import Counter

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'# Controls when to stop the loop
FIND_WORD_DICT = {}
ALL_WORD=[]
ANS_WORD =[]

def main():
    """
    TODO:
    """
    read_dictionary()
    print('Welcome to standCode "Anagram Generator" (or -1 to quit)')
    start = time.time()
    while 1:
        User_input = input('Find anagram:')
        if User_input == EXIT:
            break
        else:
           find_anagrams(User_input)

    
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open (FILE ,'r') as file:
        for line in file:
            word = line.strip()
            ALL_WORD.append(word);

            
            


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    for i in range (len(ALL_WORD)):
        if Counter(s) == Counter(ALL_WORD[i]):
            ANS_WORD.append(ALL_WORD[i])
            print("FOUND : %s",ALL_WORD[i])
    print(ANS_WORD)    
    


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    pass


if __name__ == '__main__':
    main()
