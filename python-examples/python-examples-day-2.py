"""

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and
a tuple which contains every number.Suppose the following input is supplied to the program:

34,67,55,33,12,98
Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

"""

# num = input('enter numbers').split(",")
# print(list(num))
# print(tuple(list(num)))
from math import sqrt

"""
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

"""


class StringUtil:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("enter name")

    def print_string(self):
        print(self.s.upper())

    def test_fun(self):
        self.get_string()
        self.print_string()


util = StringUtil()
# util.test_fun()

"""

Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24

"""

# def compute_formula(nums):
#     C = 50
#     H = 30
#     result = []
#     for D in nums:
#         Q = sqrt((2 - C - int(D)) / H)
#         result.append(Q)
#     return result
#
#
# d = input("Enter D value").split(",")
# print(compute_formula(d))

"""
_Write a program which takes 2 digits, 
X,Y as input and generates a 2-dimensional array.
 The element value in the i-th row and j-th column of the array should be i _ j.*
"""


# args = input("Enter value ").split(",")


def make_multi_dim_array(x, y):
    multi_dim_array = []
    for i in range(x):
        temp = list()
        for j in range(y):
            temp.append(i * j)
        multi_dim_array.append(temp)
    return multi_dim_array


# print(make_multi_dim_array(int(args[0]), int(args[1])))


def make_list_com(x, y):
    return [[i for i in range(x)] for j in range(y)]


# print(make_list_com(int(args[0]), int(args[1])))

"""
Write a program that accepts a comma separated sequence of words as input and prints the words in 
a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world
"""
# words = [x for x in input("enter words").split(",")]
# words.sort(key=len)
# print(','.join(words))

import operator

employees = [
    {'Name': 'Alan Turing', 'age': 30, 'salary': 10000},
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]


def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def cust_sort(x, y):
    if x.get('Name') == y.get('Name'):
        return x.get('age') == y.get('age')
    return x.get('Name') == y.get('Name')


# employees.sort(key=(get_name,get_age), reverse=True)
# employees.sort(key=lambda x: operator.getitem(x.get('Name'), lambda x: x.get('age')))
# employees.sort(key=cust_sort, reverse=True)
# print(employees)

"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT

"""


def inputs():
    while True:
        string = input()
        if not string:
            return
        yield string


lines = (line.upper() for line in inputs())
print(*lines, sep='\n')
