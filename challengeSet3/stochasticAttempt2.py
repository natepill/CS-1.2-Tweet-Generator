from random import randint
# from challengeSet3.histogramDict import *
import histogramDict


def file_words(text):
     word_list = histogramDict.read_txt_file(text)
     return word_list


def histogram_to_list(corpus_list):
    # print(corpus_list)
    hist = histogram(corpus_list)
    list_of_frequency = list()

    for key, value in hist.items():
        # list_of_frequency.append(key) * value
        list_of_frequency += [key for _ in range(value)]
            # list_of_frequency.append([key, value/len(corpus_list)])
            # print(new_list)
    return list_of_frequency





#Choose word with unweighted probability
# def random_word(freq_list):
#     index = randint(0, len(freq_list)-1)
#     return freq_list[index]


def random_word(histogram_dict):
    '''Random word with weighted probability'''
    counter = 0
    # Random number between 0 and the sum total of all frequencies
    hist_sum = sum(histogram_dict.values())
    rand_sum = randint(0,hist_sum - 1)


    for key, value in histogram_dict.items():
        counter += value
        if counter > rand_sum:
            return key
        else:
            continue





if __name__ == "__main__":
    corpus_list = file_words('fish.txt') #Need to integrate sys.argv[1] instead of file name
    source_text_hist = histogramDict.histogram(corpus_list)
    # print(source_text_hist)
    print(random_word(source_text_hist))
    # freq_list = histogram_to_list(corpus_list)
    # print(get_frequency(corpus_list, "fish"))
