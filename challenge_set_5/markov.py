import dictogram

class MarkovChain(dict):

    def __init__(self):
        self.corpus_histogram = Dictogram('blog-text')
        self.markov_dict = self.generate_markov(self.corpus_histogram.histogram_of_words)

        # self.wordFrequencies = Dictogram(wordsLst)
        # self._comile(wordsLst)


    def generate_markov(self, words):
        markov = {}

        for i in range(len(words)-1):
            if words[i] not in markov:
                markov[words[i]] = Dictogram()
            markov[words[i]].add_count(words[i+1])

        return markov





if __name__ == "__main__":
    mark = MarkovChain()
