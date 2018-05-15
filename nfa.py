from transition_state import *
class Nfa:
    def __init__(self, firstInput):
        startingState = TransitionState()
        startingState.values = firstInput.values

        self.currentStates = startingState.addVerticalLines()
        self.nextStates = [] # transition state type

    def consumeInput(self, inputArr):
        if len(inputArr) != 2:
            raise ValueError('Incorrect parameter for inputArr. Should be int array of length 2.')

        baseState = TransitionState()
        baseState.values = inputArr

        # Look at each old state
        for oldState in self.currentStates:
            # Concat on transition states with horizontal lines
            transStates = baseState.addHorizontal(oldState)

            # Remove duplicates in transStates

            tempArr = []
            for elem in transStates:
                tempArr = tempArr + elem.addVerticle(oldState)

            # Remove duplicates in tempArr

            # Concat next states with new states
            self.nextStates = self.nextStates + tempArr[:]

        # Copy next states into current states, clear next states
        self.currentStates = self.nextStates[:]
        self.nextStates = []