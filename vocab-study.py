# Write your own vocabulary study game:
# flash a word, player has to guess the definition, then is shown the definition.
from random import randint
import requests

from PyDictionary import PyDictionary

dictionary=PyDictionary()

def random_word():
    with open("/usr/share/dict/words") as file:
        dict = file.read().splitlines()

        return dict[randint(0, len(dict)-1)]


print("What is the definition of {}?".format(random_word()))

# user_guess = input("Definition: ")

print (dictionary.meaning(random_word()))
