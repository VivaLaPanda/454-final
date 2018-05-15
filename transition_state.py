from old_state import *
import copy

startpoint = 0
endpoint = 1
dot = 2

class TransitionState:

    values = [0, 0]
    lineH = [False, False]
    lineV = [False, False]
    pips = [startpoint, startpoint, startpoint]
    lineSegments = 0

    def __init__(self, v=None, lh=None, lv=None, ep=None, ls=0):
        if v is not None and len(v) == 2:
            self.values = v
        if lh is not None and len(lh) == 3:
            self.lineH = lh
        if lv is not None and len(lv) == 2:
            self.lineV = lv
        if ep is not None and len(ep) == 3:
            self.pips = ep

        self.lineSegments = ls

    def makeOldState(self):
        os = OldState(self.pips, self.lineV)
        return os

    def addHorizontal(self, oldState):
        newStates = []

        idx = 0
        for element in oldState.pips:
            if (element == dot):
                continue

            if idx == 0 \
                    and self.values[0] > 0 \
                    and self.lineH[0] == False:
                newState = copy.deepcopy(self)
                newState.lineH[0] = True
                newState.values[0] -= 1

                if oldState.pips[0] == startpoint:
                    newState.lineSegments += 1

                newState.pips[0] += 1

                newStates.append(newState)

            if (idx == 1
                    and self.values[0] > 0
                    and self.values[1] > 0
                    and self.lineH[1] == False):
                newState = copy.deepcopy(self)
                newState.lineH[1] = True
                newState.values[0] -= 1
                newState.values[1] -= 1

                if oldState.pips[1] == startpoint:
                    newState.lineSegments += 1

                newState.pips[1] += 1

                newStates.append(newState)

            if (idx == 2
                    and self.values[1] > 0
                    and self.lineH[2] == False):
                newState = copy.deepcopy(self)
                newState.lineH[2] = True
                newState.values[0] -= 1

                if oldState.pips[2] == startpoint:
                    newState.lineSegments += 1

                newState.pips[2] += 1

                newStates.append(newState)

        if len(newStates) == 0:
            return newStates

        for state in newStates:
            newState = state.addHorizontal(oldState)
            newStates.append(newState)

        return newStates

    def addVerticalLines(self):
        newStates = []

        for i in range(len(self.lineV)):
            if self.values[i] == 0 or self.lineV[i]:
                continue
            if self.pips[0] == dot and self.pips[1] == dot and self.pips[2] == dot:
                # if every pip is a dot, no lines can be drawn
                return []

            newTState = TransitionState(self.values[:], self.lineH[:], self.lineV[:], self.pips[:], self.lineSegments)
            newTState.lineV[i] = True
            newTState.values[i] -= 1
            # if current pip is an endpoint, it becomes a dot
            # if current pip is a startpoint, it becomes an endpoint
            newTState.pips[i]+=1
            newTState.pips[i+1]+=1

            if newTState.pips[i] == endpoint and newTState.pips[i+1] == endpoint:
                newTState.lineSegments -= 1
            if newTState.pips[i] == startpoint and newTState.pips[i + 1] == startpoint:
                newTState.lineSegments += 1

            if newTState.lineSegments > 3:
                return []

            newStates.append(newTState)

        if len(newStates) == 0:
            return []

        # make recursive call on the first element in the new states list
        # this adds the case where two vertical lines are drawn.
        newStates.extend(newStates[0].addVerticalLines())

        return newStates
