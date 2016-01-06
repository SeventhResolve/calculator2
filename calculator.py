"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculate():
    user_input = raw_input("> ")
    tokens = user_input.split(" ")
    operation = tokens[0] 
    operand1 = int(tokens[1])
    operand2 = int(tokens[2])

    if operation == "+":
        print add(operand1, operand2)
    elif operation == "-":
        print subtract(operand1, operand2)
    elif operation == "*":
        print multiply(operand1, operand2)
    elif operation == "/":
        print divide(operand1, operand2)
        
calculate()