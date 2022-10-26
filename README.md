# Route Me

Route me is a python termial program, which runs in the CI mock terminal on Heroku.
<br>
Users can create a graph and find the shortest route to their target. Users can also create a maze, they can choose to solve it them self or use the program to show them the correct path.

![Program Screen](assets/media/main_menu_img.png)

## How to use it

This program is designed to help you find the quickest way from a start position to a destination. It can also create and solve mazes. When you start the program you will be taken to the Main menu. Use the instructions and image below to help navigate.
<br>

### Main Menu

#### Option 1 - Create Maze
This will generate a random new maze. It will ask for a name and a size then create a maze with the dimensions entered.
Will the take you to the create maze menu (option 1).
#### Option 2 - Create Graph
This will create a empty graph. It will ask for a name for your graph.
Will the take you to the create graph menu (option 2).
#### Option 3 - Load Maze
This will show a list of all saved mazes and ask you to enter the name of the maze you want to load.
Will the tak you to the create maze menu (option 1).
#### Option 4 - Load Graph
This will show a list of all saved graphs and ask you to enter the name of the graph you want to load.
Will the tak you to the create graph menu (option 2).
#### Option 0 - Exit
This will terminate the program.

<br>

### Option 1 - Create Maze
#### Option 1 - Solve /Unsolve Maze
This will show the path to get from the start of the maze to the other. If they maze has already been solved it will remove the path.
#### Option 2 - Save Maze
This will save the maze to a google sheets file.
#### Option 0 - Back to Main Menu
This will take you back to the main menu.

<br>

### Option 2 - Create Graph
#### Option 1 - Add Node
This will add a node to the graph, it will ask for a name for the node.
#### Option 2 - Add Link
This will cretae a link between two nodes. It will ask for the name of the start connection and the name of the end. It will then ask for the weight for the connections. 
#### Option 3 - Delete Link
This will delete a link between two nodes. It will ask for the name of the start connection and the name of the end and set the link to 0.
#### Option 4 - Delete Node
This will remove a node from the graph and all its connections, It will ask for the name of the node to remove. 
#### Option 5 - Save Graph
This will save the graph to a google sheets file.
#### Option 6 - Show Graph Details
This will show the name of the graph, the name of the nodes and all the connections in the graph matrix. 
#### Option 7 - Fill With Sample Data
This will create a graph with test data in the nodes and connections. 
#### Option 8 - Show Connections
This will show all teh connections for one node. It will ask you to enter the name of the node.
#### Option 9 - Find Shortest Route
This will find the shortest path between two node. It will ask for the names of the start and end. Itw ill then find the route and list out the steps.
#### Option 0 - Back to menu
This will take you back to the main menu.

<br>

### Navigaton Flowchart

<br>

![Navigation Image](assets/media/route_me_menu_flow.png)

***

## User Story
|Story No.|Story|
| ------------- | ------------- |
|1| As a user, <br> I want to be able to create a randomly genrated maze <br> so that I can get see how good i am at solving them. <br><br>I know I am done when a maze is shown in the console |
|2|As a user, <br> I want to be able to choose the size of my maze <br> so that I can control the difficulty of the maze.<br><br>I know I am done when users can enter a size and a maze appears in theose dimensions.|
|3|As a user, <br> I want to be able to solve the maze<br> so that I can get the path to solve the maze. <br><br> I know I am done when a path is shown on the maze.|
|4|As a user,<br> I want to be able to save a maze <br> so that I can use it in another program or come back to it. <br> <br> I know I am done when google sheets can view a maze.|
|5|As a user,<br> I want to be able to load a maze <br> so that I can come back to it and edit it. <br> <br> I know I am done when a user can view a worksheet from google sheets.|
|6|As a user,<br> I want to be able to create a graph <br> so that I can plan a route. <br> <br> I know I am done when a user can view all the connetions in an array.|
|7|As a user,<br> I want to be able to find the shorest path between two nodes <br> so that I can find a quick route. <br> <br> I know I am done when a user can view all the steps to get from one node to another.|
|8|As a user,<br> I want to be able to save a graph <br> so that I can use it in another program or come back to it. <br> <br> I know I am done when google sheets can view a maze.|
|9|As a user,<br> I want to be able to load a graph <br> so that I can come back to it and edit it. <br> <br> I know I am done when a user can view a worksheet from google sheets.|
|10|As a user,<br> I want to be able to edit a graph <br> so that I can change it to my prefernces. <br> <br> I know I am done when a user can add and delete nodes, they will also be able to add and delete connections.|

## Features

### Menus
The main menu is the first screen you will interact with. The user will choose from 5 options in a numerical menu:
![Main menu](assets/media/main_menu_img.png)

The maze menu is the menu which shows all the things yoiu can do to a maze once it is created. The user will choose from 4 options in a numerical menu:
![Maze menu](assets/media/maze_menu_img.png)

The graph menu is the menu which shows all the things yoiu can do to a graph once it is created. The user will choose from 10 options in a numerical menu:
![Graph menu](assets/media/graph_menu_img.png)

### Create Maze
The user can give the maze a name and then set the size of the maze. Once a name that starts with a letter has been entered and a maze size between 10 and 40 has been entered it will create the maze. the maze is created using a random prims algorithm.

**Prims Algorithm **
Start with a grid full of walls.
Pick a random cell, mark it as part of the maze. Add the walls of the cell to the wall list.
While there are walls in the list:
    Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
        Make the wall a passage and mark the unvisited cell as part of the maze
        Add the neighboring walls of the cell to the wall list.
    Remove the wall from the list

![Create Maze](assets/media/create_maze_img.png)

### Solve maze/ Unsolve maze
Option 1 in the maze menu will work out the path to complete the maze. It uses a recursive method to check all possible routes until it reaches the exit of the maze. It uses a depth-first approach.

```
def __create_path(self, path, current, last, goal):
        '''
        recursive method to find a path to the exit point in the
        maze returning the path it took.

        Parameters
        ----------
        path: int[]
            steps taken to get to the exit
        current: int[]
            current position in the maze
        last: int[]
            the position in the maze it has left
        goal: int[]
            the exit to the maze

        Returns
        -------
        path: int[]
            steps to the exit
        '''
        new_path = []

        if current == goal:
            path.append(current)
            return path

        for count in range(4):
            if count == 0:
                current_coord = current[0]
                maze_edge = 0
            if count == 1:
                current_coord = current[1]
                maze_edge = 0
            if count == 2:
                current_coord = current[1]
                maze_edge = self.maze_size-1
            if count == 3:
                current_coord = current[0]
                maze_edge = self.maze_size-1

            if current_coord != maze_edge:
                next_path = self.__set_next_path(count, current)
                if next_path != last:
                    if self.maze[next_path[0]][next_path[1]] != self.__wall:
                        temp_path = self.__create_path([], next_path, current,
                                                       goal)
                        if len(temp_path) > len(new_path):
                            new_path = temp_path
                            new_path.append(current)
        return new_path
```

![Solve Maze](assets/media/solve_maze_img.png)

### Save a maze
Option 2 of the menu will save the maze to google sheets. It takes the name of the maze and create a new worksheet with the same name then will pass the array maze data to the sheets. 

![Save Maze](assets/media/saving_maze_img.png)

### Load a maze
Option 3 in the main menu will show all the available sheets that can be loaded. The user will then be able to enter the sheet name the maze will be loaded in.
 
![Load Maze](assets/media/loading_maze_img.png)

### Create Graph
Once a name that starts with a letter has been entered it will create the graph.

![Graph menu](assets/media/create_graph_img.png)

### Add node
Can add a node to the graph. It will ask the user to enter the name for the node and will check to make sure it doesnt alredy exist in the graph.

### Add/edit link
Can add a link between to nodes. It will ask for the name of the first node then the name of the second node. once it has validated both names it will ask the user to enter the weight between the nodes then finally create the link.

### Delete node
This will remove the node from the graph and all links associated to it. it will ask the user for the name of the node to remove. 

### Delete link
Can remove a link between to nodes. It will ask for the name of the first node then the name of the second node. once it has validated both names it will set the link weight to 0.

### Show graph
This will show all the details for the graph and will ask the user if they want to view the complete matrix. 

### Show connections for one node
Will ask the user to enter the name of the node they want to view. It will then show all the weights and connections for the node.

### Find the shorest path

using the Dijkstras algorithm it will find the shortest path from a start location to the end. 

The Pseudo code I used to design the methods are below. 

This will find the total distance from the start node to the end.
```
 1  function Dijkstra(Graph, source):
 2      
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8      
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12          
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]
```

This prints out the path that was taken to get to the destination. 
```
1  S ← empty sequence
2  u ← target
3  if prev[u] is defined or u = source:          // Do something only if the vertex is reachable
4      while u is defined:                       // Construct the shortest path with a stack S
5          insert u at the beginning of S        // Push the vertex onto the stack
6          u ← prev[u]                           // Traverse from target to source
```

These can be seen in the GameGraph class in methods "dijkstra_path" and "__print_short_path"

### Quick fill the graph with sample data

### Save a graph

### Load a graph

## Future features

Live solving for maze.

Different with and height for maze.

Spanning tree

None and zero.

## Data modeling

## Testing

### Manual Testing & User Story Testing
[Click here](TESTING.md)

### Validatior Testing

### Solved Bugs

https://stackoverflow.com/questions/39188827/trying-to-understand-python-loop-using-underscore-and-input

finding max

## Deployment

### Cloning & Forking
#### Fork
1. On GitHub.com, navigate to the [dlhamilton/Route Me](https://github.com/dlhamilton/route-me) repository.
2. In the top-right corner of the page, click Fork.
3. By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.
4. Add a description to your fork.
5. Click Create fork.

#### Clone
1. Above the list of files click the button that says 'Code'.
2. Copy the URL for the repository.
3. Open Terminal. Change the directory to the location where you want the cloned directory.
4. Type git clone, and then paste the URL
5. Press Enter.

### Local Deployment
1. Sign up to [Gitpod](https://gitpod.io/)
2. Download the Gitpod browser extension.
3. On GitHub.com, navigate to the [dlhamilton/route_me](https://github.com/dlhamilton/route-me) repository.
4. Above the list of files click the button that says 'Gitpod'.

### Remote Deployment 
 The site was deployed to Heroku. If you have forked/cloned the repository the steps to deploy are:
 1. On Heroku, cretae a new app.
 2. Set the buildbacks to Python and NodeJs in that order .
 3. Link your Heroku app to you repository.
 4. Click on Deploy.
 5. The page will then provide the url to the python terminal.

 The live link can be found here - [Route Me](https://github.com/dlhamilton/route-me)

***

## Credits

Code instutie for the deployment terminal

https://patorjk.com/software/taag/#p=display&f=Doom&t=Route-Me

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

https://en.wikipedia.org/wiki/Maze_generation_algorithm

-----
Happy coding!