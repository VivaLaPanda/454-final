

class OldState:

    lineV = [False, False]
    endpoint = [True, True, True]

    def __init__(self, ep=None, lv=None):
        if ep is not None and len(ep) > 0:
            self.endpoint = ep
        if lv is not None and len(lv) > 0:
            self.lineV = lv


