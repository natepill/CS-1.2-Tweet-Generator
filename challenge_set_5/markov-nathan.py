import dictogram
from dictogram import Dictogram
import sys
import random
# from dictogram import random_word

class MarkovChain(dict):

    # def __init__(self):
    #     self.corpus_histogram = Dictogram('blog-text')
    #     self.markov_dict = self.generate_markov(self.corpus_histogram.histogram_of_words)
    #
    #     # self.wordFrequencies = Dictogram(wordsLst)
    #     self._comile(wordsLst)

    # def generate_markov(self, words):
    #     markov = {}
    #     print(words)
    #
    #     # for i in range(len(words)-1):
    #     for index, key in enumerate(words):
    #         print(index, key)
    #         # print(i)
    #         # print(words[i])
    #         if words[i] not in markov:
    #             markov[words[i]] = Dictogram()
    #         markov[words[i]].add_count(words[i+1])
    #
    #     return markov



    def build_markov(self):

        with open(sys.argv[1]) as file:
            corpus = file.read().split()

        dict = {}

        i=0
        while i+1 < len(corpus):
            word = corpus[i]
            if dict.get(word) == None:
                next_word = corpus[i+1]
                list = [next_word]
                histogram = Dictogram(list)
                dict[word] = histogram
            else:
                next_word = corpus[i+1]
                dict.get(word).add_count(next_word)
            i += 1

        return dict

    def random_walk(self, dict):
        random_walk = ""
        list_of_keys = list(dict.keys())
        chosen_number = random.randint(0, len(list_of_keys)-1)
        chosen_word = list_of_keys[chosen_number]
        random_walk = random_walk + chosen_word

        for _ in range(0,20):
            dictogram = dict.get(chosen_word)
            new_word = random_word(dictogram)
            random_walk = random_walk +" "+ new_word
            chosen_word = new_word

        print(random_walk)
        return random_walk



if __name__ == '__main__':
    markov = MarkovChain()
    dict = markov.build_markov()
    print(markov.random_walk(dict))
