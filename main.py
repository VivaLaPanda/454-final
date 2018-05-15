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
        print(input_array[i])

    return

def parse_input(w):
    h = ast.literal_eval(w.replace("]","],"))
    return h

def print_output(trans_state):
    output = ""
    if trans_state.lineV[0]:
        output+= "|"
    else:
        output+=" "
    if trans_state.lineH[0]:
        output+= "_"
        output+= trans_state.values
        output+= 
    else:

    if trans_state.lineH[1]:
        return
    else:

    if trans_state.lineV[1]:
        return
    else:

    return

main()