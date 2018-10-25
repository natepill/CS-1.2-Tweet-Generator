# randomize all possiblities of a string
import sys
from collections import deque

class anagram():


    def __init__(self, word):
        self.word = word
        self.anagram_possibilities = list()



    def shift_right(self, word):
        try:
            return [word[-1]] + word[:-1]
        except IndexError:
            return word
    # https://stackoverflow.com/questions/34279048/python-move-all-elements-of-a-list-to-the-right-by-one


    def anagram(self, word):
        counter = 0

        while (counter < len(word)-1):

            shift_right(self.word)
            self.word = shift_right(word)


            # for _ in range(0, counter):
            #     # print(counter)
            #     self.word = shift_right(word)
            #     print(shift)


            anagram_possibilities.append(''.join((shift)))
            counter += 1

        # for i in range(0, len(word)-1):
        #     anagram_possibilities.append(''.join(shift_right(word)))

    anagram(list(sys.argv[1]))
    print(anagram_possibilities)
    # print(sys.argv[1])

    # def test_shift(word):
    #     return [word[-1]] + word[:-1]
