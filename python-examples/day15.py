"""Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print
the company name of a given email address. Both user names and company names are composed of letters only.
Example: If the following email address is given as input to the program"""


def get_company_name(names):
    return list(map(lambda x: str(x).split('@')[1].split('.')[0], names))


print(get_company_name(['xxx@google.com']))

"""Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example: If the following words is given as input to the program:

2 cats and 3 dogs.
Then, the output of the program should be:

['2', '3']"""


def is_num(x):
    try:
        num = int(x)
        return True
    except ValueError:
        return False


def get_number(sent):
    return list(filter(is_num, str(sent).split(' ')))


print(get_number('2 cats and 3 dogs.'))

"""Print a unicode string "hello world"."""
unicodeString = u"hello world!"
print(unicodeString.encode('utf-8'))

"""Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example: If the following n is given as input to the program:

5"""


def compute_sum(n):
    sum = float(0)
    for i in range(1,n + 1):
        sum = sum + (i / i + 1)
    return sum


print(compute_sum(5))
