from tkinter import *
from node import Node

import algorithm
import time


class GridPane(Canvas):
    def __init__(self, master, numRow, numCol, nodeSize, startPos=(-1, -1), goalPos=(-1, -1)):
        # creating a canvas
        Canvas.__init__(self, master, width=800, height=810)

        # information
        self.nodeSize = nodeSize
        self.numRow = numRow
        self.numCol = numCol
        self.width = numCol * nodeSize
        self.height = numRow * nodeSize
        self.grids = []
        self.startPos = startPos
        self.goalPos = goalPos
        self.executing = False

        # event handling
        self.bind("<ButtonPress-1>", self.onMousePressed)
        self.bind("<B1-Motion>", self.onMouseMoved)
        self.bind("<ButtonRelease-1>", self.onMouseRelease)
        self.bind("<ButtonPress-2>", self.onMouseRightClicked)
        self.dragging = False
        self.draggingNode = None

        # initializing
        self.initialize()

    def initialize(self):
        self.grids = []
        self.executing = False
        for row in range(0, self.numRow):
            line = []
            for col in range(0, self.numCol):
                nodeType = 0
                if (col, row) == self.startPos:
                    nodeType = 1
                elif (col, row) == self.goalPos:
                    nodeType == 2
                line.append(Node(col, row, accessible=True, type=nodeType))
            self.grids.append(line)
        self.show()

    def reset(self, startPos, goalPos):
        if not self.executing:
            self.startPos = startPos
            self.goalPos = goalPos
            self.initialize()

    def show(self):
        for row in self.grids:
            for n in row:
                n.show(self, "white", self.nodeSize)
        self.showStart()
        self.showGoal()

    def showStart(self):
        if self.isInsideByGrid(self.startPos[0], self.startPos[1]):
            radius = self.nodeSize // 2
            x = self.startPos[0] * self.nodeSize + radius
            y = self.startPos[1] * self.nodeSize + radius
            self.create_oval(x - radius, y - radius, x + radius, y + radius, fill="grey")
            (self.grids[self.startPos[1]][self.startPos[0]]).type = 1
            #(self.grids[self.startPos[1]][self.startPos[0]]).accessible = True

    def showGoal(self):
        if self.isInsideByGrid(self.goalPos[0], self.goalPos[1]):
            radius = self.nodeSize // 2
            x = self.goalPos[0] * self.nodeSize + radius
            y = self.goalPos[1] * self.nodeSize + radius
            self.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue")
            (self.grids[self.goalPos[1]][self.goalPos[0]]).type = 2
            #(self.grids[self.goalPos[1]][self.goalPos[0]]).accessible = True

    def clear(self):
        if self.executing:
            return
        for x in range(self.numCol):
            for y in range(self.numRow):
                node = self.getNode(x, y)
                if node.type == 0:
                    node.g = node.h = 0.0
                    node.f = float("inf")
                    node.show(self, "white", self.nodeSize)
        start = self.grids[self.startPos[1]][self.startPos[0]]
        goal = self.grids[self.goalPos[1]][self.goalPos[0]]
        start.g = start.h = goal.g = goal.f = 0.0
        start.f = goal.f = float("inf")
        goal.show(self, "white", self.nodeSize)
        self.showGoal()

    def isInsideByPix(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def isInsideByGrid(self, x, y):
        return 0 <= x < self.numCol and 0 <= y < self.numRow

    def getNeighbors(self, node):
        if node.accessible == False:
            return
        y = node.y - 1
        x = node.x - 1
        neighbors = []

        for i in range(0, 3):
            for j in range(0, 3):
                if self.isInsideByGrid(x + i, y + j):
                    n = self.grids[y + j][x + i]
                    if n.accessible:
                        neighbors.append(n)
        return neighbors

    def getNeighbors2(self, node):
        if node.accessible == False:
            return
        x = node.x
        y = node.y
        neighbors = []

        if x < self.numCol - 1 and self.grids[y][x + 1].accessible:
            neighbors.append(self.grids[y][x + 1])
        if x > 0 and self.grids[y][x - 1].accessible:
            neighbors.append(self.grids[y][x - 1])
        if y < self.numRow - 1 and self.grids[y + 1][x].accessible:
            neighbors.append(self.grids[y + 1][x])
        if y > 0 and self.grids[y - 1][x].accessible:
            neighbors.append(self.grids[y - 1][x])

        return neighbors

    def getNode(self, x, y):
        return self.grids[y][x]

    def visualize(self, algo):
        if self.executing:
            return
        case = algo.get()
        if case != None:
            self.clear()
            self.executing = True
            start = self.grids[self.startPos[1]][self.startPos[0]]
            goal = self.grids[self.goalPos[1]][self.goalPos[0]]

            if case == 0:
                algorithm.AStar(self, start, goal)
            elif case == 1:
                algorithm.dijkstra(self, start, goal)
            elif case == 2:
                algorithm.greedy(self, start, goal)
            elif case == 3:
                algorithm.bfs(self, start, goal)
            elif case == 4:
                algorithm.dfs(self,start, goal)



    def test(self):
        if self.executing:
            return
        self.clear()
        self.executing = True
        start = self.grids[self.startPos[1]][self.startPos[0]]
        goal = self.grids[self.goalPos[1]][self.goalPos[0]]
        #bfs.findPath(self, start, goal)
        #dijkstra.findPath(self, self.grids, start, goal)
        algorithm.bfs(self, start, goal)

    def onMousePressed(self, event):
        x = event.x // self.nodeSize
        y = event.y // self.nodeSize
        if self.isInsideByGrid(x, y) and not self.executing:
            node = self.getNode(x, y)
            if node.type == 0:
                node.accessible = False
                node.type = -1
                node.show(self, "black", self.nodeSize)
            else:
                self.dragging = True
                self.draggingNode = node

    def onMouseMoved(self, event):
        x = event.x // self.nodeSize
        y = event.y // self.nodeSize
        if self.isInsideByGrid(x, y) and not self.executing:
            node = self.getNode(x, y)
            if self.dragging:
                if self.draggingNode.type == 1 and (x, y) != self.goalPos:
                    oldPos = self.startPos
                    self.startPos = (x, y)
                    node.show(self, "white", self.nodeSize)
                    #node.accessible = True
                    self.showStart()
                    self.draggingNode = node

                    if self.startPos != oldPos:
                        temp = self.getNode(oldPos[0], oldPos[1])
                        color = "white"
                        type = 0
                        if temp.accessible == False:
                            color = "black"
                            type = -1
                        temp.show(self, color, self.nodeSize)
                        #temp.accessible = True
                        temp.type = type
                elif self.draggingNode.type == 2 and self.startPos != (x, y):
                    oldPos = self.goalPos
                    self.goalPos = (x, y)
                    node.show(self, "white", self.nodeSize)
                    #node.accessible = True
                    self.showGoal()
                    self.draggingNode = node

                    if self.goalPos != oldPos:
                        temp = self.getNode(oldPos[0], oldPos[1])
                        color = "white"
                        type = 0
                        if temp.accessible == False:
                            color = "black"
                            type = -1
                        temp.show(self, color, self.nodeSize)
                        #temp.accessible = True
                        temp.type = type
            elif node.type == 0:
                node.accessible = False
                node.type = -1
                node.show(self, "black", self.nodeSize)

    def onMouseRelease(self, event):
        if self.dragging and (self.draggingNode.type == 1 or self.draggingNode.type == 2):
            self.draggingNode.accessible = True
        self.dragging = False

    def onMouseRightClicked(self, event):
        x = event.x // self.nodeSize
        y = event.y // self.nodeSize

        node = self.getNode(x, y)
        node.show(self, "white", self.nodeSize)
        node.type = 0
        node.accessible = True
