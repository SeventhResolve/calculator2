"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
print """
    Welcome to calculator.  Please enter a calculation by inputting the 
    operation followed by operand(s).
    To quit, press 'q'
"""

def calculate():
    user_input = raw_input("> ")
    tokens = user_input.split(" ")
    if len(tokens) >= 2:
        operation = tokens[0] 
        operand1 = int(tokens[1])
        if len(tokens) == 3:
            operand2 = int(tokens[2])

        if operation == "+":
            print add(operand1, operand2)
            return calculate()
        elif operation == "-":
            print subtract(operand1, operand2)
            return calculate()
        elif operation == "*":
            print multiply(operand1, operand2)
            return calculate()
        elif operation == "/":
            print divide(operand1, operand2)
            return calculate()     
        elif operation == "square":
            print square(operand1)
            return calculate()
        elif operation == "cube":
            print cube(operand1)
            return calculate()
        elif operation == "pow":
            print power(operand1, operand2)
            return calculate()
        elif operation == "mod":
            print mod(operand1, operand2)   
            return calculate()

    elif len(tokens) == 1 and tokens[0] == "q":
        print "Thanks for playing!"
    else:
        print "Sorry that's not a valid entry."
        return calculate()

calculate()