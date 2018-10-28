import timeit

SETUP_CODE = """
from random import randint

import sys
"""

# open file
# Grabbed all the lines and put into array
# Choose "x" amount of words from array and print in a sentence
# Use " ".join to convert into a sentence string and print it out
# close file

TEST_CODE = """

word_num = sys.argv[1]

def dict_sentence(word_num):
    with open("/usr/share/dict/words", 'r') as file:
        dict_word = file.read().splitlines()

        # print(dict_word)


        for _ in range(int(word_num)):
            rand = randint(0, len(dict_word)-1)
            print(''.join(dict_word[rand]), end= ' ')


dict_sentence(word_num)

"""

times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          number = 100)



print('Function completed in time: {}'.format(min(times)))
