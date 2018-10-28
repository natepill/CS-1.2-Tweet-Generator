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


# url = "https://www.dictionary.com/browse/"+ str(rand_word) + "?s=t"

url = "https://www.dictionary.com/browse/Metempsychosis?s=t"



source_code =  requests.get(url)

html_text = source_code.text

soup = BeautifulSoup(html_text, "html.parser")


# print(soup.prettify())


# meaning = soup.find_all('span' {'class': 'one-click'}, limit=1)
# meaning = soup.find_all("span", {"class": "one-click"}, limit=1)
meaning = soup.find('span')
# meaning = soup.find('#initial-load-content > main > section > section > section > div.expand-container > div > section > ol > li')

# if "css-zw8qdz e10vl5dg3" in html_text:
#     print("True")

print(meaning.content)



with open('dict-entry-file', 'w') as file:
    file.write(soup.prettify())




# print(meaning)

# print (dictionary.meaning(random_word()))
