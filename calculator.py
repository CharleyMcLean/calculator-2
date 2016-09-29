"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic_further import *


# def evaluate_expression(user_string):
#     pass

def prefix_calc():
    while True:
        user_input = raw_input("> ")
        user_input_list = user_input.split(" ")
        #print user_input_list
        
        if user_input_list[0] not in ["+",'-', '/' ,'*', 'pow','mod', 'square', 'cube']:
            print "Please start with an operator."

        for user in user_input_list[1:]
            elif user_input_list[1:] 

        elif user_input_list[0] == "q":
            break
        
        elif user_input_list[0] == "+":
            return add(user_input_list[1:])
        
        elif user_input_list[0] == "-":
            return subtract((user_input_list[1: ]))
        
        elif user_input_list[0] == "*":
            return multiply(user_input_list[1:])
        
        elif user_input_list[0] == "/":
            return divide(user_input_list[1:])
        
        elif user_input_list[0] == "square":
            print square(int(user_input_list[1]))
        
        elif user_input_list[0] == "cube":
            print cube(int(user_input_list[1]))
        
        elif user_input_list[0] == "pow":
            return power(user_input_list[1:])
        
        else:
            print mod(int(user_input_list[1]), int(user_input_list[2]))



prefix_calc()

