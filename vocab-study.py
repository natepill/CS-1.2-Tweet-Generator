# Write your own vocabulary study game:
# flash a word, player has to guess the definition, then is shown the definition.
from random import randint
import requests
# import html.parser
from bs4 import BeautifulSoup

from PyDictionary import PyDictionary
dictionary=PyDictionary()



def random_word():
    with open("/usr/share/dict/words") as file:
        dict = file.read().splitlines()

        return dict[randint(0, len(dict)-1)]


rand_word = random_word()
print("What is the definition of {}?".format(rand_word))


# user_guess = input("Definition: ")


url = "https://www.dictionary.com/browse/"+ str(rand_word) + "?s=t"


source_code =  requests.get(url)

html_text = source_code.text

soup = BeautifulSoup(html_text, "html.parser")

# print(html_text)

meaning = soup.find('ol', {'class': 'css-zw8qdz e10vl5dg3'})

if "css-zw8qdz e10vl5dg3" in html_text:
    print("True")

print(meaning.content)

# print (dictionary.meaning(random_word()))
