"""
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
"""

tup_val = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tup_val[:5])
print(tup_val[5:])

"""Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,
7,8,9,10). """
even_tup = tuple(i for i in tup_val if i % 2 == 0)
print(even_tup)
print(tuple(filter(lambda a: a % 2 == 0, tup_val)))

"""Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]."""
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda a: a ** 2, num_list)))

"""Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,
5,6,7,8,9,10]. """
print(list(filter(lambda x: x % 2 == 0, list(map(lambda x: x ** 2, num_list)))))
"""Write a program which can filter() to make a list whose elements are even number between 1 and 20
"""
print(list(filter(lambda x: x % 2 == 0, range(1, 21))))
