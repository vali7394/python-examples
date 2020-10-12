"""Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
"""
elements = map(lambda x: x ** 2, range(1, 21))
print(list(elements))

"""Define a class named American which has a static method called printNationality."""


class American:
    @staticmethod
    def print_nationality():
        print("American")


American.print_nationality()


class NewYorker(American):
    def __init__(self):
        print('NewYorker')

    @staticmethod
    def print_nationality():
        print("NewYorker")


NewYorker.print_nationality()
