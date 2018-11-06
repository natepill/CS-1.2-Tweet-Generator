blog = ''

with open('blog-text') as file:
    blog = file.read().split()



def histogram(text):

    word_counter = []
    for word in text:
        if word in word_counter:

            word_counter.append()






def unique_words(histogram):
    pass


def frequency(word, histogram):
    pass



print(histogram(blog))
# print(unique_words(histogram(blog)))
# print(frequency('to', histogram(blog)))
