import sys

anagram_possibilities = list()

def shift_right(word):
    try:
        return [word[-1]] + word[:-1]
    except IndexError:
        return word


def anagram(word):

    for index, letter in enumerate(word):

        counter = 0

        while counter != len(word):
            word.insert(counter, word.pop(index))

            # for _ in range(len(word)):
            #     word[]
                #need to append all possibilities of shifted elements with a new starting character



            anagram_possibilities.append("".join(word))
            counter += 1

anagram(list("bart"))

print(anagram_possibilities)

if 'brat' in anagram_possibilities:
    print("True")
else:
    print("False")



        #swaping elements
        # word[index], word[counter] = word[counter], word[index]
