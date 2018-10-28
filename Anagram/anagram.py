import string

letters = list(string.ascii_lowercase)
list_of_anagrams = []

def letter_tracker(word):

    word = word.lower()
    alpha_dict = {}

    for letter in letters:
        alpha_dict[letter] = 0

    for letter in word:
        alpha_dict[letter] += 1

    return alpha_dict



#Make sure to make program failsafe against uppercase letters
def anagram(word):

    dict = ''

    with open('/usr/share/dict/words') as file:
        dict = file.read().splitlines()


    letters_in_word = letter_tracker(word)

    anagram_score_completed = 0
    for letter in letters_in_word:
        anagram_score_completed += letters_in_word[letter]


    for dict_word in dict:

        if dict_word.isalpha() == False:
            pass

        if len(dict_word) != len(word):
            pass

        dict_word_tracker = letter_tracker(dict_word)

        anagram_score = 0

        for letter in dict_word_tracker:

            if dict_word_tracker[letter] == letters_in_word[letter]:
                anagram_score += dict_word_tracker[letter]


        if anagram_score == anagram_score_completed:
            list_of_anagrams.append(dict_word)
        else:
            pass



anagram("bart")


print("We found {} anagrams!".format(len(list_of_anagrams)))
print(' '.join(list_of_anagrams))
