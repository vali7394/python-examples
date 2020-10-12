"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
from functools import reduce


def div_by_7_not_by_5(start, end):
    num = list()
    for i in range(start, end):
        if i % 7 == 0 and i % 5 != 0:
            num.append(i)
    return num


print(div_by_7_not_by_5(2000, 3200))

print(*(i for i in range(2000, 3200) if i % 7 == 0 and i % 5 != 0), sep=",")

"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to 
the program: 8 Then, the output should be:40320
"""


def fact(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i

    return result


def fact_rec(num):
    if num == 1: return num
    return num * fact_rec(num - 1)


def fact_input():
    while True:
        try:
            num = int(input("Enter no to cal fact"))
            break
        except ValueError:
            pass


print(fact(8))
print(fact_rec(8))


def fun_acc(acc, item):
    return acc * item


# num = int(input('enter number'))
# print(reduce(fun_acc, range(1, num + 1), 1))

"""
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is
 an integral number between 1 and n (both included). and then the program should print the dictionary.
 Suppose the following input is supplied to the program: 8
 
 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
 
"""


def create_dict(num):
    print({i: i * i for i in range(1, num + 1)})


create_dict(8)


def create_enum(no):
    map = dict()
    for index, value in enumerate(range(1, no + 1),start=1):
        map[index] = value*value

    print(map)


print(create_enum(8))
