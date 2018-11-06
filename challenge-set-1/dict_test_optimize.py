import timeit

# SETUP_CODE = """
from random import randint

import sys


# open file
# Grabbed all the lines and put into array
# Choose "x" amount of words from array and print in a sentence
# Use " ".join to convert into a sentence string and print it out
# close file
 # """



# TEST_CODE = """



def dict_sentence(word_num):

    """
    """
    with open("/usr/share/dict/words") as file:
        dict_words = file.read().splitlines()

    random_num_array = list() #line numbers that I want to read

    for _ in range(int(word_num)):
        random_num_array.append(randint(0, len(dict_words)-1))

    # print(dict_word)
    # for num in range(int(word_num)):

    for rand in random_num_array:
        print(''.join(dict_words[rand]), end= ' ')


word_num = sys.argv[1]

dict_sentence(word_num)
# print("hello")

# """


#
# times = timeit.repeat(setup = SETUP_CODE,
#                           stmt = TEST_CODE,
#                           number = 1)
#
#
#
# print('Function completed in time: {}'.format(min(times)))
