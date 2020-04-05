# Path-finding Visualization
This is a python3 program with a GUI which you can interact with. You can modify the board, like creating obstacles and moving start and/or goal positioins, and choose a path-finding algorithm to see how that algorithm finds a path from start to goal and how the path looks like.  

## How to use?
Modify the board:
* Left-click a white grid or left-click and drag your mouse to create obstacles on the board.  
* Left-click and drag the start/goal node to change the starting/ending position.
* Click "Reset board" to reset the board to default status
* Click "Clear board" to remove all the path and visited nodes but keep the start and goal node and the obstacles you created

Once you have finished modifying the board, you can selecte an algorithm then press the "Visualize" button to see the visualization.

Note that while visualizing the process, user cannot make any changes to the map and press any buttons.

## Demo
### A* algorithm:
![AStar](https://github.com/Beeno5920/pathfindingVisualization/blob/master/Demo/AStar.gif)  
Shortest path guaranteed

### Dijkstra's algorithm:
![Dijkstra](https://github.com/Beeno5920/pathfindingVisualization/blob/master/Demo/dijkstra.gif)  
Shortest path guaranteed

### Greedy algorithm:
![Greedy](https://github.com/Beeno5920/pathfindingVisualization/blob/master/Demo/greedy.gif)  
-- Recently added --

### Breadth-first search algoritm:
![bfs](https://github.com/Beeno5920/pathfindingVisualization/blob/master/Demo/bfs.gif)  
Shortest path obtained in this case since the weight between each accessible node is defaulted to be 1

### Depth-first search algorithm:
![dfs](https://github.com/Beeno5920/pathfindingVisualization/blob/master/Demo/dfs.gif)  
Paths obtained by this algorithm may not be the shortest path

### No path:
![no path](https://github.com/Beeno5920/pathfindingVisualization/blob/master/Demo/noPath.gif)  
 
