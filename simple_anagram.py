import sys


    def shift_right(word):
        try:
            return [word[-1]] + word[:-1]
        except IndexError:
            return word
    # https://stackoverflow.com/questions/34279048/python-move-all-elements-of-a-list-to-the-right-by-one


    def anagram(word):
        counter = 0

        anagram_possibilities = list()

        while (counter < len(word)-1):

            shift_right(word)
            word = shift_right(word)


            for _ in range(0, counter):
                # print(counter)
                self.word = shift_right(word)
                print(shift)


            anagram_possibilities.append(''.join((shift)))
            counter += 1
