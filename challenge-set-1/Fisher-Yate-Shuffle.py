import random

def shuffle_array(array):
    length = len(array)
    shuffled = 1

    while (shuffled != length):

        unshuffled = random.randint(0, (length) - shuffled)

        # print(array[unshuffled])
        temp_value = array[unshuffled]

        array[unshuffled] = array[-shuffled]
        array[-shuffled] = temp_value

        # print(array[-shuffled])

        shuffled += 1
    #
    # for i in range(len(array)-1, 0, -1):
    #
    #     unshuffled = random.randint(0, (length) - shuffled)


an_array = [0,1,2,3,4,5,6,7,8,9]
shuffle_array(an_array)

print(an_array)
