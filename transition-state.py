from OldState import *


class TransitionState:

    values = [0, 0]
    lineH = [False, False]
    lineV = [False, False]
    endpoint = [True, True, True]

    def __init__(self, v=None, lh=None, lv=None, ep=None):
        if v is not None and len(v) > 0:
            self.values = v
        if lh is not None and len(lh) > 0:
            self.lineH = lh
        if lv is not None and len(lv) > 0:
            self.lineV = lv
        if ep is not None and len(ep) > 0:
            self.endpoint = ep

    def makeOldState(self):
        os = OldState(self.endpoint, self.lineV)
        return os


