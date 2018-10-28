blog = ''

with open('blog-text') as file:
    blog = file.read().split()


def histogram(text):

    words = []
    words_tuple =[]

    for word in text:
        words.append([word, 1])

    occurs = 0
    for word in text:
        for word_list in words:
            if word_list[0] == word:
                occurs += 1
        words_tuple.append((word, occurs))
        occurs = 0


    return words_tuple



def unique_words(histogram):
    # takes a histogram argument and returns the total count of unique words in the histogram.
    unique_count = 0
    for word in histogram:
        unique_count += 1
    return unique_count


def frequency(word, histogram):
    # takes a word and histogram argument and returns the number of times that word appears in a text.
    for occurence in histogram:
        if word == occurence[0]:
            return occurence[1]



# print(histogram(blog))
print(unique_words(histogram(blog)))
# print(frequency('to', histogram(blog)))
