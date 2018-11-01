from random import randint
from histogramDict import *

# histogram = histogram-dict.histogram(str(sys.argv[1]))

#TODO Make function truly pick a random word based upon frequency
def file_words(text):
     word_list = read_txt_file(text)
     return word_list


def histogram_to_list(corpus_list):
    # print(corpus_list)
    hist = histogram(corpus_list)
    list_of_frequency = list()


    for key, value in hist.items():
        # list_of_frequency.append(key) * value
        new_list = [list_of_frequency.append(key) for _ in range(value)]
        # list_of_frequency.append([key, value/len(corpus_list)])
        # print(new_list)
    return list_of_frequency


def random_word(freq_list):
    index = randint(0, len(freq_list)-1)
    return freq_list[index]

def weighted_choice(weights):
    values = [] # 2,5,10
    running_total = 0 #10

    for w in weights:
        running_total += w
        values.append(running_total)

    rnd = random.random() * running_total
    for i, value in enumerate(values):
        if rnd < value:
            return weights[i]
            #https://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python

def true_random_selection(freq_weight, word):
    pass


    # Generate a number between 0 and 1.
    # Walk the list substracting the probability of each item from your number.
    # Pick the item that, after substraction, took your number down to 0 or below.


if __name__ == '__main__':

    corpus_list = file_words('fish.txt') #Need to integrate sys.argv[1] instead of file name
    freq_list = histogram_to_list(corpus_list)
    # print(weighted_choice())
    print(random_word(freq_list))
