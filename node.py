import math

class Node:
    def __init__(self, x, y, accessible = True, weight = 1, type = 0):
        # coordinates
        self.x = x  # col
        self.y = y  # row

        # costs
        self.h = 0.0    # cost from this node to goal
        self.g = 0.0    # cost from start to this node
        self.f = float("inf")    # total cost from start to this node

        # status
        self.accessible = accessible
        self.previous = None
        self.type = type   # 0 : node, 1 : start, 2 : goal, -1 : block
        self.weight = weight

    def show(self, screen, color, nodeSize):
        x0 = self.x * nodeSize
        x1 = x0 + nodeSize
        y0 = self.y * nodeSize
        y1 = y0 + nodeSize

        screen.create_rectangle(x0, y0, x1, y1, fill=color, outline="grey")

    def heuristic(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

