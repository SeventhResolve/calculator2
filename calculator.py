"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
user_input = raw_input("> ")
tokens = user_input.split(" ")
operation = tokens[0] 
operation1 = int(tokens[1])
operation2 = int(tokens[2])

if operation == "+":
    print add(operation1, operation2)