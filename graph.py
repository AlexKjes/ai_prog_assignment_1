

class Node:

    def __init__(self, state, g, h, parent=None):
        self.state = state
        self.g = g
        self.h = h

        self.parent = parent
        self.children = []

    def get_weight(self):
        return self.g + self.h
