from tkinter import *
from tkinter import ttk
from gridPane import GridPane
from node import Node

SCREEN_WIDTH = 800

planeSize = (50, 50)
nodeSize = SCREEN_WIDTH // planeSize[1]

startPos = (planeSize[0] // 4, planeSize[1] // 2)
goalPos = (planeSize[0] // 4 * 3, planeSize[1] // 2)

bgColor = "#%02x%02x%02x" % (230, 230, 230)

root = Tk()
root.title("Path-finding Algorithms Visualizer")

plane = GridPane(root, planeSize[0], planeSize[1], nodeSize, startPos=startPos, goalPos=goalPos)

setting = Frame(root, width=200, height=810)

instructions = Canvas(setting, height=350)
instructions.create_text(145, 15, font=("Verdana Bold", 25), text="----- Instructions -----")
instructions.create_oval(50, 60, 70, 80, fill="grey")
instructions.create_oval(50, 90, 70, 110, fill="blue")
instructions.create_rectangle(50, 120, 70, 140, fill="black", outline="grey")
instructions.create_rectangle(50, 150, 70, 170, fill="#%02x%02x%02x" % (102, 255, 153), outline="grey")
instructions.create_rectangle(50, 180, 70, 200, fill="yellow", outline="grey")
instructions.create_text(135, 70, font=("Verdana", 20), text="    =    Start")
instructions.create_text(135, 100, font=("Verdana", 20), text="   =    Goal")
instructions.create_text(155, 130, font=("Verdana", 20), text=" =  Obstacle")
instructions.create_text(155, 160, font=("Verdana", 20), text="      =  Visited node")
instructions.create_text(155, 190, font=("Verdana", 20), text="   =  Path node")
instructions.create_text(130, 280, font=("Verdana", 15), text="- Click or drag the white node to\n create obstacles\n\n"
                                                              "- Drag the start or goal node to\n change its position\n"
                                                              "\n- Right click to remove an obstacle\n")
instructions.create_text(135, 340, font=("Verdana", 25), text="--------------------------")

blank1 = Label(setting)

algo = IntVar()
label = Label(setting, text="Choose an algorithm:", font=("Verdana Bold", 20), bg="#%02x%02x%02x" % (230, 230, 230))
AStarButton = Radiobutton(setting, text="A*", font=("Verdana", 15), variable=algo, value=0)
dijkstraButton = Radiobutton(setting, text="Dijkstra's", font=("Verdana", 15), variable=algo, value=1)
greedyButton = Radiobutton(setting, text="Greedy", font=("Verdana", 15), variable=algo, value=2)
bfsButton = Radiobutton(setting, text="Bread-first search", font=("Verdana", 15), variable=algo, value=3)
dfsButton = Radiobutton(setting, text="Depth-first search", font=("Verdana", 15), variable=algo, value=4)

blank2 = Label(setting)

visualize = Button(setting, text="Visualize", font=("Verdana", 20), command=lambda: plane.visualize(algo), pady=10)
clear = Button(setting, text="Clear board", font=("Verdana", 20), command=plane.clear, pady=10)
reset = Button(setting, text="Reset board", font=("Verdana", 20), command=lambda: plane.reset(startPos, goalPos), pady=10)


plane.grid(row=0, column=0)
setting.grid(row=0, column=1)

instructions.pack(fill=BOTH, expand=True)

blank1.pack()

label.pack(fill=BOTH, expand=True)
AStarButton.pack(fill=BOTH, expand=True)
dijkstraButton.pack(fill=BOTH, expand=True)
greedyButton.pack(fill=BOTH, expand=True)
bfsButton.pack(fill=BOTH, expand=True)
dfsButton.pack(fill=BOTH, expand=True)

blank2.pack()

visualize.pack(fill=BOTH, expand=True)
clear.pack(side=RIGHT, fill=BOTH, expand=True)
reset.pack(fill=BOTH, expand=True)

root.mainloop()