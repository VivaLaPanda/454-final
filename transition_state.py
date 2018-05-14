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
        # TODO: test this function. 
        newStates = []

        for i in range(len(self.lineV)):
            if newTState.values[i] == 0 or newTState.lineV[i] == 0:
                return
            if not self.pips[0] and not self.pips[1] and not self.pips[2]:
                # dot => 0, so if every pip is a dot
                return

            newTState = TransitionState(self.values, self.lineH, self.lineV, self.pips, self.lineSegments)
            newTState.lineV[i] = True
            newTState.values[i] -= 1
            if newTState.pips[i] == endpoint: # if current pip is an endpoint, it becomes a dot
                newTState.pips[i] = dot
            if newTState.pips[i] == startpoint: # if currrent pip is a startpoint, it becomes an endpoint
                newTState.pips[i] = endpoint

            if newTState.pips[i+1] == endpoint: # sames goes for connecting pip
                newTState.pips[i+1] = dot
            if newTState.pips[i+1] == startpoint:
                newTState.pips[i+1] = endpoint

            if newTState.pips[i] == endpoint and newTState.pips[i+1] == endpoint:
                newTState.lineSegments -= 1
            if newTState.pips[i] == startpoint and newTState.pips[i + 1] == startpoint:
                newTState.lineSegments += 1

            if newTState.lineSegments > 3:
                return

            newStates.append(newTState)

        if len(newStates) == 0:
            return

        newStates.extend(self.addVerticalLines())

        return newStates

