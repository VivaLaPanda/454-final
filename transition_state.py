from old_state import *
import copy

startpoint = 0
endpoint = 1
dot = 2

class TransitionState:

    def __init__(self, v=None, lh=None, lv=None, ep=None, ls=0, viewValues=None):
        self.values = [0, 0]
        self.lineH = [False, False, False]
        self.lineV = [False, False]
        self.pips = [startpoint, startpoint, startpoint]
        self.lineSegments = 0
        self.parent = None

        if v is not None and len(v) == 2:
            self.values = v
        if lh is not None and len(lh) == 3:
            self.lineH = lh
        if lv is not None and len(lv) == 2:
            self.lineV = lv
        if ep is not None and len(ep) == 3:
            self.pips = ep

        if viewValues == None:
            self.viewvalues = self.values[:]
        else:
            self.viewvalues = viewValues[:]
        self.lineSegments = ls

    def makeOldState(self):
        os = OldState(self.pips, self.lineV)
        return os

    def addHorizontal(self, oldState, depth=0):
        newStates = []

        idx = 0
        for oldPip in oldState.pips:
            if (oldPip == dot):
                idx += 1
                continue

            if (depth == 0 and oldPip == startpoint):
                idx += 1
                continue

            if idx == 0 \
                    and self.values[0] != 0 \
                    and self.lineH[0] == False:
                newState = copy.deepcopy(self)

                newState.lineH[0] = True
                newState.values[0] -= 1

                if oldState.pips[0] == startpoint:
                    newState.lineSegments += 1

                newState.pips[0] += 1

                if not newState.lineSegments > 2:
                    newStates.append(newState)

            if (idx == 1
                    and self.values[0] != 0
                    and self.values[1] != 0
                    and self.lineH[1] == False):
                newState = copy.deepcopy(self)

                newState.lineH[1] = True
                newState.values[0] -= 1
                newState.values[1] -= 1

                if oldState.pips[1] == startpoint:
                    newState.lineSegments += 1

                newState.pips[1] += 1

                if not newState.lineSegments > 2:
                    newStates.append(newState)

            if (idx == 2
                    and self.values[1] != 0
                    and self.lineH[2] == False):
                newState = copy.deepcopy(self)

                newState.lineH[2] = True
                newState.values[1] -= 1

                if oldState.pips[2] == startpoint:
                    newState.lineSegments += 1

                newState.pips[2] += 1

                if not newState.lineSegments > 2:
                    newStates.append(newState)

            idx += 1

        if len(newStates) == 0:
            return newStates

        for state in newStates:
            childStates = state.addHorizontal(oldState, depth + 1)
            newStates.extend(childStates)

        return newStates

    def addVerticalLines(self):
        newStates = []

        for i in range(len(self.lineV)):
            if self.values[i] == 0 or self.lineV[i]:
                continue
            if self.pips[0] == dot and self.pips[1] == dot and self.pips[2] == dot:
                # if every pip is a dot, no lines can be drawn
                return []

            newTState = TransitionState(self.values[:], self.lineH[:], self.lineV[:], self.pips[:], self.lineSegments, self.viewvalues)
            newTState.lineV[i] = True
            newTState.values[i] -= 1

            if newTState.pips[i] == endpoint and newTState.pips[i+1] == endpoint:
                newTState.lineSegments -= 1
            if newTState.pips[i] == startpoint and newTState.pips[i + 1] == startpoint:
                newTState.lineSegments += 1

            # if current pip is an endpoint, it becomes a dot
            # if current pip is a startpoint, it becomes an endpoint
            newTState.pips[i]+=1
            newTState.pips[i+1]+=1

            if newTState.lineSegments > 3:
                return []

            newStates.append(newTState)

        if len(newStates) == 0:
            return []

        # make recursive call on the first element in the new states list
        # this adds the case where two vertical lines are drawn.
        newStates.extend(newStates[0].addVerticalLines())

        return newStates