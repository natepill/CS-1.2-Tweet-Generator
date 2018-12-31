from dictogram import Dictogram
from rando_word import random_word
import random
import sys


class MarkovChain:

    def build_markov(self):
        markovChain = {}
        with open(sys.argv[1]) as file:
            corpus = file.read().split()

        i=0
        while i+1 < len(corpus): #go through whole corpus
            word = corpus[i]
            if markovChain.get(word) == None:
                next_word = corpus[i+1]
                list = [next_word]
                histogram = Dictogram(list)
                markovChain[word] = histogram
            else:
                next_word = corpus[i+1]
                markovChain.get(word).add_count(next_word)
            i += 1

        return markovChain


    def secondOrderMarkovChain(self):

        with open(sys.argv[1]) as file:
            corpus = file.read().split()

            markovChain = {}


            i = 0

            while i+2 < len(corpus):
                segment = (corpus[i], corpus[i+1])
                if markovChain.get(segment) == None:
                    next_word = list(corpus[i+2])
                    histogram = Dictogram(next_word)
                    markovChain[segment] = histogram
                else:
                    next_word = corpus[i+2]
                    markovChain.get(segment).add_count(next_word)
                i += 1

        return markovChain

    # def secondOrderSentence(self, markovChain):
    #
    #     sentence = ""
    #     list_of_keys = list(markovChain.keys())
    #     segment = list_of_keys[random.randint(0, len(list_of_keys)-1)]
    #     sentence = sentence + segment[0] + segment[1]
    #
    #     for _ in range(0,40):
    #         dictogram = markovChain.get(segment)
    #         new_word = random_word(self, dictogram)
    #         sentence = sentence +" "+ new_word
    #         segment = (segment[1], new_word)
    #
    #     print(sentence)
    #     return sentence


    def nth_order_markov(order, text_list):
        """ this function takes in a word and checks to see what words come after it
        to determine the word sequence for our generated markov chain"""
        markov_dict = dict()
        # for each word in list, key is word and value is dictogram
        for index in range(len(text_list) - order):
            # text_list[index] should be our word from list
            window = tuple(text_list[index: index + order])
            # check if key is stored already
            if window in markov_dict:
                # if it is, then append it to the existing histogram
                markov_dict[window].add_count([text_list[index + order]])
            else:
                # if not, create new entry with window as key and dictogram as value
                markov_dict[window] = Dictogram([text_list[index + order]])
        # return dictionary
        return markov_dict








    def generate_sentence(self, dict):
        sentence = ""
        list_of_keys = list(dict.keys())
        index = random.randint(0, len(list_of_keys)-1)
        chosen_word = list_of_keys[index]
        sentence = sentence + chosen_word

        for _ in range(0,20):
            dictogram = dict.get(chosen_word)
            print(dictogram)
            new_word = random_word(self, dictogram)
            sentence = sentence +" "+ new_word
            chosen_word = new_word

        print(sentence)
        return sentence



if __name__ == '__main__':
    markov = MarkovChain()
    dict = markov.secondOrderMarkovChain()
    markov.secondOrderSentence(dict)
