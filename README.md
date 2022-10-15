# Route Me

Route me is a python termial program, which runs in the CI mock terminal on Heroku.
<br>
Users can create a graph and find the shortest route to their target. Users can also create a maze, they can choose to solve it them self or use the program to show them the correct path.

![imaage](image)

## How to use it

This program is designed o help you find the quickest way from a start position to a destination. It can also create and solve mazes. When you start the program you will be taken to the Main menu. Use the instructions and image below to help navigate.
<br>

### Main Menu

#### Option 1 - Create Maze
This will generate a random new maze. It will ask for a name and a size then create a maze with the dimensions entered.
#### Option 2 - Create Graph
This will create a empty graph. It will ask for a name for your graph. 
#### Option 3 - Load Maze
This will show a list of all saved mazes and ask you to enter the name of the maze you want to load.
#### Option 4 - Load Graph
This will show a list of all saved graphs and ask you to enter the name of the graph you want to load.
#### Option 0 - Exit
This will terminate the program.

<br>

### Option 1 - Create Maze
#### Option 1 - Solve /Unsolve Maze
#### Option 2 - Save Maze
#### Option 0 - Back to Main Menu

<br>

### Option 2 - Create Graph
#### Option 1 - Add Node
#### Option 2 - Add Link
#### Option 3 - Delete Link
#### Option 4 - Delete Node
#### Option 5 - Save Graph
#### Option 6 - Show Graph Details
#### Option 7 - Fill With Sample Data
#### Option 8 - Show Connections
#### Option 9 - Find Shortest Route
#### Option 0 - Back to menu

<br>

### Option 3 -Load Graph

<br>

### Option 4 - Load Maze

### Navigaton Flowchart

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

MENUS

create maze

Maze size

solve maze

unsolve maze

save a maze

load a maze


create graph

add node

add/edit link

delete node

delete link

show graph

show connections for one node

find the shorest path 

quick fill the graph with sample data

name the graph

save a graph

load a graph

## Future features

Different with and height for maze.

Live solving for maze.

## Data modeling

## Testing

### Manual Testing

Test the pathing works

Test the maze solving works

Test a add, edit, delete for connections

test a add and delete of a node

### User Story Testing

|Story No.|Result|Story/ Evidence|
| ------------- | ------------- | ------------- |
|1|Test Pass| As a user, <br> I want to be able to create a randomly genrated maze <br> so that I can get see how good i am at solving them. <br><br>I know I am done when a maze is shown in the console <br><br>Evidence:<br>The user can open the high score modal and it loads the scores from local storage.<br> ![high_score](assets/media/chrome_images/game_highscore.webp)|
|2|Test Pass|As a user, <br> I want to be able to choose the size of my maze <br> so that I can control the difficulty of the maze.<br><br>I know I am done when users can enter a size and a maze appears in theose dimensions.<br><br>Evidence:<br>The user can open the high score modal and it loads the scores from local storage.<br> ![high_score](assets/media/chrome_images/game_highscore.webp)|
|3|Test Pass|As a user, <br> I want to be able to solve the maze<br> so that I can get the path to solve the maze. <br><br> I know I am done when a path is shown on the maze.<br><br>Evidence:<br>The user can open the high score modal and it loads the scores from local storage.<br> ![high_score](assets/media/chrome_images/game_highscore.webp)|
|4|Test Pass|As a user,<br> I want to be able to save a maze <br> so that I can use it in another program or come back to it. <br> <br> I know I am done when google sheets can view a maze.<br><br>Evidence:<br>The user can open the high score modal and it loads the scores from local storage.<br> ![high_score](assets/media/chrome_images/game_highscore.webp)|
|5|Test Pass|As a user,<br> I want to be able to load a maze <br> so that I can come back to it and edit it. <br> <br> I know I am done when a user can view a worksheet from google sheets.<br><br>Evidence:<br>The user can open the high score modal and it loads the scores from local storage.<br> ![high_score](assets/media/chrome_images/game_highscore.webp)|
|6|Test Pass|As a user,<br> I want to be able to create a graph <br> so that I can plan a route. <br> <br> I know I am done when a user can view all the connetions in an array.<br><br>Evidence:<br>The user can open the high score modal and it loads the scores from local storage.<br> ![high_score](assets/media/chrome_images/game_highscore.webp)|
|7|Test Pass|As a user,<br> I want to be able to find the shorest path between two nodes <br> so that I can find a quick route. <br> <br> I know I am done when a user can view all the steps to get from one node to another.<br><br>Evidence:<br>The user can open the high score modal and it loads the scores from local storage.<br> ![high_score](assets/media/chrome_images/game_highscore.webp)|
|8|Test Pass|As a user,<br> I want to be able to save a graph <br> so that I can use it in another program or come back to it. <br> <br> I know I am done when google sheets can view a maze.<br><br>Evidence:<br>The user can open the high score modal and it loads the scores from local storage.<br> ![high_score](assets/media/chrome_images/game_highscore.webp)|
|9|Test Pass|As a user,<br> I want to be able to load a graph <br> so that I can come back to it and edit it. <br> <br> I know I am done when a user can view a worksheet from google sheets.<br><br>Evidence:<br>The user can open the high score modal and it loads the scores from local storage.<br> ![high_score](assets/media/chrome_images/game_highscore.webp)|
|10|Test Pass|As a user,<br> I want to be able to edit a graph <br> so that I can change it to my prefernces. <br> <br> I know I am done when a user can add and delete nodes, they will also be able to add and delete connections.<br><br>Evidence:<br>The user can open the high score modal and it loads the scores from local storage.<br> ![high_score](assets/media/chrome_images/game_highscore.webp)|

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

-----
Happy coding!