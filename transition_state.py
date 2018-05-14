from OldState import *

dot = 0
endpoint = 1
startpoint = 2

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
        os = OldState(self.endpoint, self.lineV)
        return os

    def addHorizontal(self):

    def addVerticalLines(self):
        newStates = []

        for i in range(len(self.lineV)):
            if self.values[i] == 0 or self.lineV[idx]:
                return
            if not self.pips[0] and not self.pips[1] and not self.pips[2]:
                return

            newTState = TransitionState(self.values, self.lineH, self.lineV, self.pips)
            newTState.lineV[i] = True
            newTState.values[i] -= 1
            if newTState.lineH[i]:
                newTState.pips[i] = False
            if newTState.lineH[i+1]:
                newTState.pips[i+1] = False
            if newTState.lineV[0] and newTState.lineV[1]:
                newTState.pips[1] = False

            newStates.append(newTState)

        if len(newStates) == 0:
            return

        newStates.extend(self.addVerticalLines())

        return newStates

