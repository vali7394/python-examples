"""Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the
values are square of keys. """

values = {num: num ** 2 for num in range(1, 21)}
print(values.keys())

"""Define a function which can generate a dictionary where the keys are numbers between 1 and 20
 (both included) and the values are square of keys. The function should just print the keys only."""

"""Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (
both included). """

squares = [i ** 2 for i in range(1, 21)]
print(squares)
for i in range(5):
    print(squares[i])

print(squares[:5])
print(squares[-5:])
print(squares[5:])
"""Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the last 5 elements in the list.
"""

tuple_sqs = tuple(i**2 for i in range(1,21))
print(tuple_sqs)