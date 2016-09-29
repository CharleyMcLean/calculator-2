"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic2 import *


# def evaluate_expression(user_string):
#     pass

def prefix_calc():
    while True:
        user_input = raw_input("> ")
        user_input_list = user_input.split(" ")
        #print user_input_list
        if user_input_list[0] == "q":
            break
        elif user_input_list[0] == "+":
            print add(int(user_input_list[1]), int(user_input_list[2]))
        elif user_input_list[0] == "-":
            print subtract(int(user_input_list[1]), int(user_input_list[2]))
        elif user_input_list[0] == "*":
            print multiply(int(user_input_list[1]), int(user_input_list[2]))
        elif user_input_list[0] == "/":
            print divide(int(user_input_list[1]), int(user_input_list[2]))
        elif user_input_list[0] == "square":
            print square(int(user_input_list[1]))
        elif user_input_list[0] == "cube":
            print cube(int(user_input_list[1]))
        elif user_input_list[0] == "pow":
            print power(int(user_input_list[1]), int(user_input_list[2]))
        else:
            print mod(int(user_input_list[1]), int(user_input_list[2]))



prefix_calc()

