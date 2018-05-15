from nfa import *
from transition_state import *
import re
import ast

def main():

    w = input("please put in your encoeded string ")
    input_array = list(parse_input(w))
    print (input_array)
    snake_nfa = Nfa()
    for i in range(len(input_array)):
        snake_nfa.consumeInput(input_array[i])
        print (input_array[i])

    return

def parse_input(w):
    h = ast.literal_eval(w.replace("]","],"))
    return h

def print_output():

    return

main()