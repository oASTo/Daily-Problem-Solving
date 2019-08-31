
# Hi, here's your problem today. This problem was recently asked by LinkedIn:
# You are given a positive integer N which represents the number of steps in a staircase.
# You can either climb 1 or 2 steps at a time.
# Write a function that returns the number of unique ways to climb the stairs.

import random


def staircase(n):
    total = 0
    for i in range(n):
        total += random.randint(1, 2)

    return total
  # Fill this in.


print(staircase(4))
# 5
print(staircase(5))
# 8
