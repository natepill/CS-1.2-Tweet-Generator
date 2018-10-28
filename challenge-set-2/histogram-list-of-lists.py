import sys

text = ''

with open(sys.argv[1]) as file:
    text = file.read().split()

# print(blog)

def histogram(text):
 # stores each unique word along with the number of times the word appears in the source text
    blog_words = []

    for word in text:

        if word not in blog_words:
            blog_words.append([word, 1])


        #Ensures that there are no repeated words being incremented/added to the list
        #We create an occurence of the word and initially increment it at 1
        #Then we check blog words to see if the word already is being tracked, and if it is, we increment its counter
        for occurence in blog_words:
            if occurence[0] == word:
                occurence[1] += 1

    return blog_words



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



# print(histogram(sys.argv[1]))
# print(unique_words(histogram(sys.argv[1])))
# print(frequency('the', histogram(sys.argv[1])))
