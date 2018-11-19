import sys
from random import randint


class Dictogram():

    def __init__(self, file_name):
        self.corpus = self.read_txt_file(file_name)
        self.histogram_of_words = self.histogram(self.corpus)

    # reads in a text files, returns a list
    def read_txt_file(self, file_name):
        with open(file_name) as file:
            corpus_list = file.read().split()
            return corpus_list

    def histogram(self, corpus_list):
     # stores each unique word along with the number of times the word appears in the source text
        histo = {}

        for word in corpus_list:
            histo[word] = 0
        for word in corpus_list:
            histo[word] += 1

        return histo

    def random_word(self, histogram_dict):
        '''Random word with weighted probability'''
        counter = 0
        # Random number between 0 and the sum total of all frequencies
        hist_sum = sum(histogram_dict.values())
        rand_sum = randint(0,hist_sum - 1)

        for key, value in histogram_dict.items():
            counter += value
            if counter > rand_sum:
                return key
            else:
                continue


    def unique_words(self):
        # takes a histogram argument and returns the total count of unique words in the histogram.
        # return histogram.keys()
        unique_count = 0
        for word in self.histogram_of_words:
            unique_count += 1
        return unique_count


    def frequency(self, word, histogram):
        # takes a word and histogram argument and returns the number of times that word appears in a text.
        return self.histogram_of_words[word]




if __name__ == "__main__":
    blog = Dictogram('blog-text')
    blog.histogram(blog.corpus)
    # print(blog.histogram_of_words)
    # print(blog.frequency('is', blog.histogram_of_words))
    print(blog.random_word(blog.histogram_of_words))


# print(histogram(blog))
# print(unique_words(histogram(blog)))
# print(frequency('was', histogram(blog)))
