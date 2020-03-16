# Path-finding Visualization
This is an app that allows user to creat obstacles on the map, then find the path from the starting point to the destination 
and visualize the path-finding process.

## How to use?
User can left-click or left-click and drag the white grid to create obstacle(s) as many as possible on the map. Positions of 
the starting point and the destination can be changed by dragging these two nodes to any grid on the map.

Once user has finished modifying the map, user can selecte an algorithm then press the "Visualize" button to see how the 
selected path-finding algorithm finds out the path from start to goal.

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

### Breadth-first search algoritm:
![bfs](https://github.com/Beeno5920/pathfindingVisualization/blob/master/Demo/bfs.gif)  
Shortest path obtained in this case since the weight between each accessible node is defaulted to be 1

### Depth-first search algorithm:
![dfs](https://github.com/Beeno5920/pathfindingVisualization/blob/master/Demo/dfs.gif)  
Paths obtained by this algorithm may not be the shortest path

### No path:
![no path](https://github.com/Beeno5920/pathfindingVisualization/blob/master/Demo/noPath.gif)  
 
