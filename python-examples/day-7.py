"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Suppose the following input is supplied to the program:

7
Then, the output should be:

0
7
14
"""

from math import sqrt


class CustomGen:

    def cus_gen_div_by_7(self, n):
        for i in range(n):
            if i % 7 == 0:
                yield i


cusGen = CustomGen()
# n = input("Enter end  range")
for i in cusGen.cus_gen_div_by_7(int(10)):
    print(i)

"""
A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a 
sequence of movement and original point. If the distance is a float, then just print the nearest integer. 
Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:

2

"""


def robo_dis_from_orig(directions):
    x, y = 0, 0
    for i in directions:
        if 'UP'.__eq__(str(i[0])):
            y += int(i[1])
        if 'DOWN'.__eq__(str(i[0])):
            y -= int(i[1])
        if 'LEFT'.__eq__(str(i[0])):
            x -= int(i[1])
        if 'RIGHT'.__eq__(str(i[0])):
            x += int(i[1])

    return int(sqrt(x * x + y * y))


directions = [('UP', 5), ('DOWN', 3), ('LEFT', 3), ('RIGHT', 2)]
print(robo_dis_from_orig(directions))
