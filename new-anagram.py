import sys

anagram_possibilities = list()

def anagram(word):

    for index, letter in enumerate(word):

        counter = 0

        while counter != len(word):
            word.insert(counter, word.pop(index))
            # l.insert(newindex, l.pop(oldindex)) trying to insert element and delete old placement
            # print(word)
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
