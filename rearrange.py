import random
import sys

arg_list = sys.argv
del arg_list[0]

rearranged_list = list()


while len(arg_list) != 0:
    random_index = random.randint(0, len(arg_list)-1)
    rearranged_list.append(arg_list.pop(random_index))

print(rearranged_list)

# for arg in rearranged_list:
#     print(arg, end=" ")
