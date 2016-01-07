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

def tokenize_input():
    """ Asks for user input and tokenizes input """

    user_input = raw_input("> ")
    tokens = user_input.split(" ")
    
    if len(tokens) >= 2:
        operation = tokens[0] 
        operand1 = tokens[1:]
        print type(operand1)
        #operand1 = float(tokens[1])
        if len(tokens) == 3:
            operand2 = float(tokens[2])

# Next steps:
# 1. Going further: Start at step #1 
# 2. Clean up tokens
# 3. Refactor operations


#         if operation == "+":
#             add_sum = add(operand1)
#             print add_sum
#             return calculate()
#         elif operation == "-":        
#             sub = int(subtract(operand1, operand2))
#             print sub
#             return calculate()
#         elif operation == "*":
#             result = int(multiply(operand1, operand2))
#             print result
#             return calculate()
#         elif operation == "/":
#             print divide(operand1, operand2)
#             return calculate()     
#         elif operation == "square":
#             print square(operand1)
#             return calculate()
#         elif operation == "cube":
#             print cube(operand1)
#             return calculate()
#         elif operation == "pow":
#             print power(operand1, operand2)
#             return calculate()
#         elif operation == "mod":
#             result_mod = int(mod(operand1, operand2))
#             print result_mod
#             return calculate()

#     elif len(tokens) == 1 and tokens[0] == "q":
#         print "Thanks for playing!"
#     else:
#         print "Sorry that's not a valid entry."
#         return calculate()

# calculate()