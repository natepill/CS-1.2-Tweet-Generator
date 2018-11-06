# Tutorial: https://www.youtube.com/watch?v=3dt4OGnU5sM

nums = [1,2,3,4,5,6,7,8,9,10]

# my_list = list()
# for number in nums:
#     my_list.append(number)

#LIST COMPREHENSION
# my_list = [number for number in nums]
# number is what we are returning to my_list
# print(my_list)

#-----------------------------------------------------------------------------------------------------------------

# my_list = list()
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

#LIST COMPREHENSION
# my_list = [n*n for n in nums]
# print(my_list)
#-----------------------------------------------------------------------------------------------------------------

# Using a map + lambda
# my_list = map(lambda n: n*n, nums) #Dont need this because of list comprehensions
# print(my_list)


#-----------------------------------------------------------------------------------------------------------------

# I want 'n' for each 'n' in nums if 'n' is even
# my_list = list()
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

#LIST COMPREHENSION
# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

#-----------------------------------------------------------------------------------------------------------------

# I want a (letter, number) pair for each letter in a 'abcd' and each number in '0123'

# my_list = list()
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)


#LIST COMPREHENSION

my_list = [(letter, number) for letter in 'abcd' for number in range(4)]


print(my_list)
