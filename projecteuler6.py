# -*- coding: utf-8 -*-
"""
@author: Jonty
"""

""" Project Euler, problem 6: """

def sum_of_squares(n):
    # finding the sum of squares of the first n natural numbers
    return sum(i**2 for i in range(1,n+1))

def square_of_sum(n):
    # finding the square of the sum of the first n natural numbers
    return sum(i for i in range(1,n+1))**2

def difference(n):
    # finding the difference between the sum of squares and square of the sum
    return  square_of_sum(n) - sum_of_squares(n)

print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is %s." % difference(100))
