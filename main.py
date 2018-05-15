import ast

from nfa import *


def main():

    w = input("please put in your encoeded string ")
    input_array = list(parse_input(w))
    print(input_array)
    snake_nfa = Nfa(input_array[0])
    for i in range(len(input_array)):
        snake_nfa.consumeInput(input_array[i])
        # print(input_array[i])
    if (len(snake_nfa.currentStates) > 0):
        print('yes')
    else:
        print('no')
    # if (len(snake_nfa.currentStates) > 0):
    #     for i in range(len(snake_nfa.currentStates)):
    #         if snake_nfa.currentStates[i].lineSegments == 1:
    #             print_output(snake_nfa.currentStates[i])
    return

def parse_input(w):
    h = ast.literal_eval(w.replace("]","],"))
    return h

def print_output(trans_state):
    output0 = ""
    output1 = ""
    output2 = ""
    output3 = ""
    output4 = ""
    parent = trans_state
    parent_list = []

    while (parent != None):
        parent_list.insert(0,parent)
        parent = parent.parent

    if parent_list[0].lineV[0]:
        output1 += "|"
    else:
        output1 += " "
    if parent_list[0].lineV[1]:
        output1 += "|"
    else:
        output1 += " "
    for i in range(len(parent_list)-1):

        #output1+= str(parent_list[i+1].viewvalues[0]) + " "
        #output2+= str(parent_list[i+1].viewvalues[1]) + " "


        if parent_list[i+1].lineH[0]:
            output0 += "\t--"
        else:
            output0 += "\t"

        if parent_list[i+1].viewvalues[0] == -1:
            output1 += "\t  "
        else:
            output1 += "\t " + str(parent_list[i+1].viewvalues[0])

        if parent_list[i+1].lineV[0]:
            output1 += "|"
        else:
            output1 += " "


        if parent_list[i+1].lineH[1]:
            output2 += "\t--"
        else:
            output2 += "\t   "

        if parent_list[i+1].viewvalues[1] == -1:
            output3 += "\t  "
        else:
            output3 += "\t " + str(parent_list[i+1].viewvalues[1])

        if parent_list[i+1].lineV[1]:
            output3 += "|"
        else:
            output3 += " "

        if parent_list[i+1].lineH[2]:
            output4 += "\t--"
        else:
            output4 += "\t   "




    print()
    print(output0)
    print()
    print(output1)
    print()
    print(output2)
    print()
    print(output3)
    print()
    print(output4)
    print()
    print()
    print()
    print()
    return

main()