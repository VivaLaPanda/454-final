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
    output0 = ""
    output1 = ""
    output2 = ""
    parent = trans_state
    while (parent != None):


        if parent.lineH[0]:
            output0 += " ___"
        else:
            output0 += "    "
        if parent.lineV[1]:
            output1 += "|"
        else:
            output1 += " "

        if parent.lineH[0]:
            output1 += "_" + str(parent.values[0]) + "_"
        else:
            output1 += " " + str(parent.values[0]) + " "

        if parent.lineV[2]:
            output2 += "|"
        else:
            output2 += " "

        if parent.lineH[1]:
            output1 += "_" + str(parent.values[1]) + "_"
        else:
            output1 += " " + str(parent.values[1]) + " "

        parent = parent.parent
    output0.replace("-1"," ")
    output1.replace("-1"," ")
    output2.replace("-1"," ")

    print(output0)
    print(output1)
    print(output2)
    return

main()