from transition_state import *
class Nfa:
    def __init__(self, firstInput):
        startingState = TransitionState()
        startingState.values = firstInput
        startingState.viewvalues = firstInput[:]

        self.currentStates = startingState.addVerticalLines()
        self.nextStates = [] # transition state type

    def consumeInput(self, inputArr):
        if len(inputArr) != 2:
            raise ValueError('Incorrect parameter for inputArr. Should be int array of length 2.')

        baseState = TransitionState()
        baseState.values = inputArr[:]
        baseState.viewvalues = inputArr[:]

        # Look at each old state
        for oldState in self.currentStates:
            # Concat on transition states with horizontal lines
            transStates = baseState.addHorizontal(oldState)

            # Remove duplicates in transStates
            newDict = dict()
            for obj in transStates:
                if tuple(obj.lineH+obj.lineV) not in newDict:
                    newDict[tuple(obj.lineH+obj.lineV)] = obj

            transStates = []
            for key, value in newDict.items():
                temp = value
                transStates.append(temp)

            tempArr = []
            for elem in transStates:
                tempArr = tempArr + elem.addVerticalLines()

            # Remove duplicates in tempArr
            for element in tempArr:
                element.parent = oldState
            # Concat next states with new states
            self.nextStates = self.nextStates + tempArr[:]

        newDict = dict()
        for obj in self.nextStates:
            if tuple(obj.lineH + obj.lineV) not in newDict:
                newDict[tuple(obj.lineH + obj.lineV)] = obj

        self.nextStates = []
        for key, value in newDict.items():
            temp = value
            self.nextStates.append(temp)

        # Copy next states into current states, clear next states
        self.currentStates = self.nextStates[:]
        self.nextStates = []