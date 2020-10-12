"""
Question:
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""

from collections import Counter


def compute_freq_of_words_in_sent(sentence):
    words = [word for word in str(sentence).split(' ')]
    freq_map = {}
    for word in words:
        if word in freq_map:
            freq_map[word] = freq_map.get(word) + 1
        else:
            freq_map[word] = 1
    freq_map = sorted(freq_map.items())
    for i in freq_map:
        print(i[0], i[1])


inpt = """New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:"""
compute_freq_of_words_in_sent(inpt)
elements = inpt.split()
words = Counter(elements)  # returns key & frequency as a dictionary
ss = sorted(words.items())  # returns as a tuple list

# for i in ss:
#     print("%s:%d"%(i[0],i[1]))


"""
Write a method which can calculate square value of number
"""


def cal_sqr(n):
    return n ** 2


# n = int(input('enter'))
print(cal_sqr(10))

"""
Python has many built-in functions, and if you do not know how to use it, you can read document online or find 
some books. But Python has a built-in document function for every built-in functions. 

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function


"""

print(help(abs))
print(dir(abs))
print(abs.__doc__)
print(pow.__doc__)

"""
Define a class, which have a class parameter and have a same instance parameter.
"""


class Demo:
    n = 0

    def __init__(self, n):
        self.n = n


demo = Demo(10)
print(demo.n)
print(Demo.n)

class Car:
    name = "Car"

    def __init__(self,name = None):
        self.name = name

honda=Car("Honda")
print("%s name is %s"%(Car.name,honda.name))

toyota=Car()
toyota.name="Toyota"
print("%s name is %s"%(Car.name,toyota.name))