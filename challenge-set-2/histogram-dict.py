

blog = ''

with open('blog-text') as file:
    blog = file.read().split()

def histogram(text):
 # stores each unique word along with the number of times the word appears in the source text
    blog_words = {}

    for word in blog:
        blog_words[word] = 0

    for word in blog:
        if word in blog_words:
            blog_words[word] += 1

    return blog_words




def unique_words(histogram):
    # takes a histogram argument and returns the total count of unique words in the histogram.
    unique_count = 0
    for word in histogram:
        unique_count += 1
    return unique_count


def frequency(word, histogram):
    # takes a word and histogram argument and returns the number of times that word appears in a text.
    return histogram[word]



# histogram(blog)
# print(unique_words(histogram(blog)))
# print(frequency('was', histogram(blog)))
