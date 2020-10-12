"""
Write a program that accepts a sequence of whitespace separated
words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world

"""

# words = {word for word in input("Enter data").split(' ')}
# words = sorted(words)
# print(' '.join(words))

"""
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and 
then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
Notes: Assume the data is input by console.


"""


def div_by_5(nums):
    values = list()
    for i in nums:
        if int(i, 2) % 5 == 0:
            values.append(i)
    return values


nums = []  # input('enter data').split(',')
print(div_by_5(nums))
print([i for i in nums if int(i, 2) % 5 == 0])
print(list(filter(lambda i: int(i, 2) % 5 == 0, nums)))

"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""


def find_even_dig():
    result = list()
    for i in range(1000, 3000):
        all_even = True
        for j in str(i):
            if int(j) % 2 != 0:
                all_even = False
        if all_even: result.append(i)
    return result


# print(find_even_dig())

"""
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
"""


def find_char_type(sentence):
    char_type_dict = {"DIGITS": 0, "LETTERS": 0}
    for i in sentence:
        if i.isnumeric():
            char_type_dict["DIGITS"] += 1
        else:
            char_type_dict["LETTERS"] += 1
    return char_type_dict


sen = input("Input please")
result = find_char_type(sen)
print(f'DIGITS {result["DIGITS"]}')
print(f'LETTERS {result["LETTERS"]}')
