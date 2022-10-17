"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        if (len(numbers) % 2) != 0:
            middleval = math.trunc(len(numbers)/2)
            print(numbers[middleval])
        else:
            listlen = len(numbers)
            half = int(listlen/2)
            median = (numbers[half] + numbers[half-1])/2
            print(median)
            
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

