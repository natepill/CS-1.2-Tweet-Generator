import sys


def shift_right(word):
    try:
        return [word[-1]] + word[:-1]
    except IndexError:
        return word
# NOT CORRECT METHOD ^^^^ WE ARE NOT TRYING TO SHIFT CHARCTERS TO THE RIGHT, WE ARE TRYING TO REARRANGE THEM

def anagram(word):
    counter = 0

    anagram_possibilities = list()

    while (counter < len(word)-1):

        # word = shift_right(word)

        for _ in range(len(word)-1):
            # print(counter)
            word = shift_right(word)
            anagram_possibilities.append(''.join((word)))

        counter += 1

    print(' '.join(anagram_possibilities))
    return anagram_possibilities




anagram(list(sys.argv[1]))
