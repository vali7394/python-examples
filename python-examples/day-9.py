"""
Define a function which can compute the sum of two numbers.
"""


def sum(a, b):
    return a + b


print(sum(10, 15))

sum_2 = lambda a, b: a + b
print(sum_2(10, 15))

"""
Define a function that can convert a integer into a string and print it in console.
"""
n = lambda a: str(a)
print(n(10))

"""
Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.
"""

compute_sum = lambda a, b: int(a) + int(b)
print(compute_sum('10', '15'))

"""
Define a function that can accept two strings as input and concatenate them and then print it in console.
"""

concat = lambda a, b: a + b
print(concat('a', 'b'))

"""
Define a function that can accept two strings as input and print the string with maximum length in console.
 If two strings have the same length, then the function should print all strings line by line.
"""
max_len = lambda a, b: max((a,b),key=len) if len(a) != len(b) else a + b
print(max_len('aaa', 'bb'))
print(max_len('aaa', 'bbb'))
