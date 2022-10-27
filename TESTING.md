# Route Me Testing

[<< Back to ReadMe](README.md)

## Manual Testing

Below are the test to check all validation and operation of the program.

### Main menu tests
<table>
    <tr>
        <th>Test Number</th>
        <th>Test</th>
        <th>Test data</th>
        <th>Expected result</th>
        <th>Actual result</th>
        <th>Test result</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Program starting</td>
        <td>n/a</td>
        <td>Loads main menu</td>
        <td>Main menu is shown to screen</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Main Menu Validation</td>
        <td>Input " "</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Main Menu Validation</td>
        <td>Input "a"</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Main Menu Validation</td>
        <td>Input 20</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Main Menu Validation</td>
        <td>Input "$"</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Main Menu Validation</td>
        <td>Input 0</td>
        <td>exits the program</td>
        <td>shows the exit screen</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Main Menu Validation</td>
        <td>Input 1</td>
        <td>Starts to create the maze</td>
        <td>Ask the user for the name of the maze</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Main Menu Validation</td>
        <td>Input 2</td>
        <td>Starts to create the graph</td>
        <td>Ask the user for the name of the graph</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Main Menu Validation</td>
        <td>Input 3</td>
        <td>Starts to load in a maze</td>
        <td>shows the user all the saved mazes</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Main Menu Validation</td>
        <td>Input 4</td>
        <td>Starts to load in a graph</td>
        <td>shows the user all the saved graphs</td>
        <td>Pass</td>
    </tr>
<table>

### Maze create tests

<table>
    <tr>
        <th>Test Number</th>
        <th>Test</th>
        <th>Test data</th>
        <th>Expected result</th>
        <th>Actual result</th>
        <th>Test result</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Maze name validating</td>
        <td>Input "test"</td>
        <td>Accepts the name and move to next screen</td>
        <td>asks the user to enter the maze size</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Maze name validating</td>
        <td>Input 2</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Maze name validating</td>
        <td>Input ""</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Maze name validating</td>
        <td>Input "£"</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Maze size validating</td>
        <td>Input "£"</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Maze size validating</td>
        <td>Input 0</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Maze size validating</td>
        <td>Input "a"</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Maze size validating</td>
        <td>Input 12</td>
        <td>Build the maze with the correct size</td>
        <td>Tells the user to press enter to see maze</td>
        <td>Pass</td>
    </tr>
</table>

### Maze menu tests

<table>
    <tr>
        <th>Test Number</th>
        <th>Test</th>
        <th>Test data</th>
        <th>Expected result</th>
        <th>Actual result</th>
        <th>Test result</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Maze menu validating</td>
        <td>Input "£"</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Maze menu validating</td>
        <td>Input -1</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Maze menu validating</td>
        <td>Input "a"</td>
        <td>Error message</td>
        <td>Error messge and interates the question</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Maze menu validating</td>
        <td>Input 1</td>
        <td>If the mave has not been solved will show the path. If it is solved it will remove the path</td>
        <td>Removes and add the solve path at the correct condition</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Maze menu validating</td>
        <td>Input 2</td>
        <td>Should save the maze data to google sheets</td>
        <td>Starts the save process</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Maze menu validating</td>
        <td>Input 3</td>
        <td>the user can start trying to solve the maze</td>
        <td>Starts the user solving process</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Maze menu validating</td>
        <td>Input 0</td>
        <td>Takes the user back to the main menu</td>
        <td>Takes the user back to the main menu</td>
        <td>Pass</td>
    </tr>
</table>

### Solve maze tests

### Save maze tests

### User solve tests

Test the pathing works

Test the maze solving works

Test a add, edit, delete for connections

test a add and delete of a node

## User Story Testing

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