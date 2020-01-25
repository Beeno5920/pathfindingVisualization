from priorityQueue import PriorityQueue
from tkinter import *
from node import Node


def AStar(screen, start, goal):
    if start == None or goal == None:
        return

    visited = []
    toExplore = PriorityQueue()
    found = False
    colorVal = "#%02x%02x%02x" % (102, 255, 153)

    visited.append(start)
    toExplore.add(start)
    start.f = 0.0

    while not toExplore.isEmpty() and not found:
        currNode = toExplore.dequeue()
        visited.append(currNode)
        currNode.show(screen, colorVal, screen.nodeSize)
        if currNode.type == 1:
            screen.showStart()
        if currNode.type == 2:
            found = True
            screen.showGoal()
            showPath(screen, goal)
            break
        neighbors = screen.getNeighbors2(currNode)

        for neighbor in neighbors:
            cost = currNode.g + neighbor.weight
            heuristic = neighbor.heuristic(goal)
            if cost + heuristic < neighbor.f:
                neighbor.g = cost
                neighbor.h = heuristic
                neighbor.f = cost + heuristic
                neighbor.previous = currNode
                toExplore.add(neighbor)

        screen.update()

    if not found:
        failToFind(visited, screen, screen.nodeSize)


def dijkstra(screen, start, goal):
    if start == None or goal == None:
        return

    visited = []
    toExplore = PriorityQueue()
    found = False
    colorVal = "#%02x%02x%02x" % (102, 255, 153)

    visited.append(start)
    toExplore.add(start)
    start.g = start.f = 0.0

    while not toExplore.isEmpty() and not found:
        currNode = toExplore.dequeue()
        visited.append(currNode)
        currNode.show(screen, colorVal, screen.nodeSize)
        if currNode.type == 1:
            screen.showStart()
        if currNode.type == 2:
            found = True
            screen.showGoal()
            showPath(screen, goal)
            break
        neighbors = screen.getNeighbors2(currNode)

        for neighbor in neighbors:
            if neighbor not in visited:
                if currNode.f + neighbor.weight < neighbor.f:
                    neighbor.g = currNode.f + neighbor.weight
                    neighbor.f = neighbor.g
                    neighbor.previous = currNode
                    toExplore.add(neighbor)
        # time.sleep(0.1)
        screen.update()

    if not found:
        failToFind(visited, screen, screen.nodeSize)


def bfs(screen, start, goal):
    if start == None or goal == None:
        return

    visited = []
    toExplore = []
    found = False
    colorVal = "#%02x%02x%02x" % (102, 255, 153)

    visited.append(start)
    toExplore.append(start)

    while len(toExplore) > 0 and not found:
        currNode = toExplore.pop(0)
        currNode.show(screen, colorVal, screen.nodeSize)
        if currNode.type == 1:
            screen.showStart()
        if currNode.type == 2:
            found = True
            screen.showGoal()
            showPath(screen, goal)
            break
        neighbors = screen.getNeighbors2(currNode)

        for neighbor in neighbors:
            if not neighbor in visited:
                neighbor.previous = currNode
                visited.append(neighbor)
                toExplore.append(neighbor)
                if neighbor.type == 2:
                    screen.showGoal()
        # time.sleep(0.2)
        screen.update()

    if not found:
        failToFind(visited, screen, screen.nodeSize)


def dfs(screen, start, goal):
    if start == None or goal == None:
        return

    visited = []
    toExplore = []
    found = False
    colorVal = "#%02x%02x%02x" % (102, 255, 153)

    visited.append(start)
    toExplore.append(start)

    while len(toExplore) > 0 and not found:
        currNode = toExplore.pop()
        currNode.show(screen, colorVal, screen.nodeSize)
        if currNode.type == 1:
            screen.showStart()
        if currNode.type == 2:
            found = True
            screen.showGoal()
            showPath(screen, goal)
            break
        neighbors = screen.getNeighbors2(currNode)

        for neighbor in neighbors:
            if not neighbor in visited:
                neighbor.previous = currNode
                visited.append(neighbor)
                toExplore.append(neighbor)
                if neighbor.type == 2:
                    screen.showGoal()
        # time.sleep(0)
        screen.update()

    if not found:
        failToFind(visited, screen, screen.nodeSize)


def showPath(screen, goal):
    path = []
    currNode = goal

    while currNode != None:
        path.append(currNode)
        currNode = currNode.previous

    path.reverse()
    for i in range(len(path)):
        path[i].show(screen, "yellow", screen.nodeSize)
        if i == 0:
            screen.showStart()
        if i == len(path) - 1:
            screen.showGoal()
        screen.update()

    screen.executing = False


def failToFind(visited, screen, nodeSize):
    screen.executing = False
    for cell in visited:
        cell.show(screen, "red", nodeSize)
    screen.showStart()
    screen.update()

    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text="Unable to find a path!", font=("Verdana", 20))
    label.pack(fill=BOTH)

    def on_closing():
        popup.destroy()
        screen.initialize()

    ok = Button(popup, text="ok", command=on_closing, width=20)
    ok.pack(fill=BOTH)

    popup.protocol("WM_DELETE_WINDOW", on_closing)
    popup.mainloop()
