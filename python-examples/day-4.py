"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9

"""

from functools import reduce


def count(sen):
    upperCount = 0
    lowerCount = 0
    for i in sen:
        if str(i).isupper():
            upperCount += 1
        elif str(i).islower():
            lowerCount += 1
    return upperCount, lowerCount


def find_type_sen(sen):
    upperCount = 0
    lowerCount = 0
    for i in sen:
        if str(i).isupper():
            upperCount += 1
        elif str(i).islower():
            lowerCount += 1
    return upperCount, lowerCount


sen = "enter"
result = find_type_sen(sen)
print(f'Upper Count {result[0]}')
print(f'Lower Count {result[1]}')

"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106
"""


def compute(num):
    exp = str('a+aa+aaa+aaaa').replace('a', num).split("+")
    result = 0
    for i in exp:
        result += int(i)
    return result

def reduce_fn(num):
    exp = str('a+aa+aaa+aaaa').replace('a', num).split("+")
    result = 0
    for i in exp:
        result += i
    return result

print(compute(input('enter')))