'''
route-me
'''
# # Library for INT_MAX
import sys
import random
import re
import gspread
from google.oauth2.service_account import Credentials
from colorama import init, Fore, Back
init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('route_me_data')


class GameMaze:
    '''
    Maze Class
    ...

    Attributes
    ----------
    maze_name : str
        name of the maze
    walls : int[]
        the array of wall in the maze
    maze : str[]
        the maze cells
    loaded : boolean
        has the maze been saved before
    solver_current
        if the maze has been attempted to be solvved and where they
        currenlty are in the maze
    maze_size
        the size of the maze


    Methods
    -------
    info(additional=""):
        Prints the person's name and age.

    __random_maze_path_creator:
        calls all the methods to create a maze

    __create_blank_maze:
        creates an array with a size of maze size

    __starting_maze_generation_position:
        gets the starting posititon for maze creation

    __get_starting_walls(start_h, start_w):
        add the walls to the walls list

    __set_starting_walls(start_h, start_w):
        set the display of the maze to show the walls

    __make_maze_walls:
        prims algorithm to make maze

    __set_left_wall(rand_wall):
        create a wall to the left of the current position

    __set_right_wall(rand_wall):
        create a wall to the right of the current position

    __set_bottom_wall(rand_wall):
        create a wall under the current position

    __set_top_wall(rand_wall):
        create a wall above the current position

    __remove_complete_wall(rand_wall):
        remove the wall from the not proccessed wall array

    draw_maze:
        draw the grid to the console

    __surrounding_cells(rand_wall):
        count all paths surrounding the wall

    __fill_open_maze_walls:
        fill the open maze items will the wall icons

    __create_ins_and_outs:
        set the entrance and exit of the maze

    solve_maze:
        will find the path to get to the end of the maze

    __get_start_and_end:
        will find the start and end coordinates

    __create_path(path, current, last, goal)
        recursive method to find a path to the exit

    __set_next_path(count, current):
        set the next coordiante that the maze should try to go

    __remove_from_maze(maze_type):
        find the solution in the array and change to path

    save_maze:
        store the maze details to google sheets

    load_in_maze(name, matrix, current):
        update the graph with the data from google

    user_solve_maze:
        using the WASD keys user can solve

    __set_user_path(direction, current):
        sets the game maze array path to the user move character
    '''
    # class attribute
    __path = 'P'
    __wall = 'W'
    __open = "O"
    __solution = "A"
    __user_move = "U"

    def __init__(self, maze_size, name):
        '''
        Constructs all the necessary attributes for the maze object.
        ...

        Parameters
        ----------
            name : str
                name of the maze
            maze_size : str
                size of the maze
        '''
        # instance attribute
        self.maze_name = name
        self.walls = []
        self.maze = []
        self.loaded = False
        self.solver_current = None
        self.maze_size = maze_size
        self.__create_blank_maze()
        self.__random_maze_path_creator()

    def __random_maze_path_creator(self):
        '''
        calls all the methods to create a maze

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        start_pos_h = \
            self.__starting_maze_generation_position()
        start_pos_w = \
            self.__starting_maze_generation_position()
        self.maze[start_pos_h][start_pos_w] = self.__path
        self.__get_starting_walls(start_pos_h, start_pos_w)
        self.__set_starting_walls(start_pos_h, start_pos_w)
        self.__make_maze_walls()
        self.__fill_open_maze_walls()
        self.__create_ins_and_outs()

    def __create_blank_maze(self):
        """
        creates an array with a size of the width and height of the maze

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        width = self.maze_size
        height = self.maze_size
        for _ in range(0, height):
            row = []
            for _ in range(0, width):
                row.append(self.__open)
            self.maze.append(row)

    def __starting_maze_generation_position(self):
        '''
        Gets the starting posititon for maze creation but stays away
        from the edge of the maze

        selects a random number between 0 and maze size - 1

        Parameters
        ----------
        None

        Returns
        -------
        starting_pos: int
            returns an int between 1 and maze size - 2
        '''
        starting_pos = int(random.random() * self.maze_size)
        if starting_pos == 0:
            starting_pos += 1
        if starting_pos == self.maze_size-1:
            starting_pos -= 1
        return starting_pos

    def __get_starting_walls(self, start_h, start_w):
        '''
        add the walls surrounding the starting path to the walls list

        Parameters
        ----------
        start_h: int
            x coordinate of starting position
        start_w: int
            y coordinate of starting position

        Returns
        -------
        None
        '''
        self.walls.append([start_h-1, start_w])
        self.walls.append([start_h, start_w-1])
        self.walls.append([start_h, start_w+1])
        self.walls.append([start_h+1, start_w])

    def __set_starting_walls(self, start_h, start_w):
        '''
        set the display of the maze to show the walls

        Parameters
        ----------
        start_h: int
            x coordinate of starting position
        start_w: int
            y coordinate of starting position

        Returns
        -------
        None
        '''
        self.maze[start_h-1][start_w] = self.__wall
        self.maze[start_h][start_w-1] = self.__wall
        self.maze[start_h][start_w+1] = self.__wall
        self.maze[start_h+1][start_w] = self.__wall

    def __make_maze_walls(self):
        '''
        Prims Algorithm
        While there are walls in the list:
        Pick a random wall from the list. If only one of the two cells that
        the wall divides is visited, then:
        Make the wall a passage and mark the unvisited cell as part of the maze
        Add the neighboring walls of the cell to the wall list.
        Remove the wall from the list

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        surrounding_cell_count = 0
        while self.walls:
            # Pick a random wall
            rand_wall = self.walls[int(random.random()*len(self.walls))-1]

            # Check if it is a left wall
            if rand_wall[1] != 0:
                if self.maze[rand_wall[0]][rand_wall[1]-1] == self.__open and \
                      self.maze[rand_wall[0]][rand_wall[1]+1] == self.__path:
                    surrounding_cell_count = \
                        self.__surrounding_cells(rand_wall)
                    if surrounding_cell_count < 2:
                        self.maze[rand_wall[0]][rand_wall[1]] = self.__path
                        # Make the walls
                        # The top wall
                        self.__set_top_wall(rand_wall)
                        # Bottom wall
                        self.__set_bottom_wall(rand_wall)
                        # left wall
                        self.__set_left_wall(rand_wall)
                    # Delete wall
                    self.__remove_complete_wall(rand_wall)
                    continue

            # Check if it is a top wall
            if rand_wall[0] != 0:
                if self.maze[rand_wall[0]-1][rand_wall[1]] == self.__open and \
                        self.maze[rand_wall[0]+1][rand_wall[1]] == self.__path:
                    surrounding_cell_count = \
                        self.__surrounding_cells(rand_wall)
                    if surrounding_cell_count < 2:
                        self.maze[rand_wall[0]][rand_wall[1]] = self.__path
                        # Make the walls
                        # top wall
                        self.__set_top_wall(rand_wall)
                        # left wall
                        self.__set_left_wall(rand_wall)
                        # right wall
                        self.__set_right_wall(rand_wall)
                    # Delete wall
                    self.__remove_complete_wall(rand_wall)
                    continue

            # Check if it is a bottom wall
            if rand_wall[0] != self.maze_size - 1:
                if self.maze[rand_wall[0]+1][rand_wall[1]] == self.__open and \
                        self.maze[rand_wall[0]-1][rand_wall[1]] == self.__path:
                    surrounding_cell_count = \
                        self.__surrounding_cells(rand_wall)
                    if surrounding_cell_count < 2:
                        self.maze[rand_wall[0]][rand_wall[1]] = self.__path
                        # Make the walls
                        # bottom wall
                        self.__set_bottom_wall(rand_wall)
                        # left wall
                        self.__set_left_wall(rand_wall)
                        # right wall
                        self.__set_right_wall(rand_wall)
                    # Delete wall
                    self.__remove_complete_wall(rand_wall)
                    continue

            # Check if it is a right wall
            if rand_wall[1] != self.maze_size-1:
                if self.maze[rand_wall[0]][rand_wall[1]+1] == self.__open and \
                        self.maze[rand_wall[0]][rand_wall[1]-1] == self.__path:
                    surrounding_cell_count = \
                        self.__surrounding_cells(rand_wall)
                    if surrounding_cell_count < 2:
                        self.maze[rand_wall[0]][rand_wall[1]] = self.__path
                        # Make the walls
                        # right wall
                        self.__set_right_wall(rand_wall)
                        # bottom wall
                        self.__set_bottom_wall(rand_wall)
                        # top wall
                        self.__set_top_wall(rand_wall)
            # Delete wall
            self.__remove_complete_wall(rand_wall)
            continue

    def __set_left_wall(self, rand_wall):
        '''
        create a wall to the left of the current position
        if it is not part of the path

        Parameters
        ----------
        rand_wall: int[]
            randomly selected wall

        Returns
        -------
        None
        '''
        if rand_wall[1] != 0:
            if (self.maze[rand_wall[0]][rand_wall[1]-1] !=
               self.__path):
                self.maze[rand_wall[0]][rand_wall[1]-1] = \
                    self.__wall
            if ([rand_wall[0], rand_wall[1]-1] not in
               self.walls):
                self.walls.\
                        append([rand_wall[0], rand_wall[1]-1])

    def __set_right_wall(self, rand_wall):
        '''
        Will create a wall to the right of the current position
        if it is not part of the path

        Parameters
        ----------
        rand_wall: int[]
            randomly selected wall

        Returns
        -------
        None
        '''
        if rand_wall[1] != self.maze_size-1:
            if (self.maze[rand_wall[0]][rand_wall[1]+1]
               != self.__path):
                self.maze[rand_wall[0]][rand_wall[1]+1] = \
                    self.__wall
            if ([rand_wall[0], rand_wall[1]+1] not in
               self.walls):
                self.walls.\
                    append([rand_wall[0], rand_wall[1]+1])

    def __set_bottom_wall(self, rand_wall):
        '''
        Will create a wall under the current position
        if it is not part of the path

        Parameters
        ----------
        rand_wall: int[]
            randomly selected wall

        Returns
        -------
        None
        '''
        if rand_wall[0] != self.maze_size-1:
            if (self.maze[rand_wall[0]+1][rand_wall[1]]
               != self.__path):
                self.maze[rand_wall[0]+1][rand_wall[1]] = \
                    self.__wall
            if ([rand_wall[0]+1, rand_wall[1]] not in
               self.walls):
                self.walls.\
                    append([rand_wall[0]+1, rand_wall[1]])

    def __set_top_wall(self, rand_wall):
        '''
        Will create a wall above the current position
        if it is not part of the path

        Parameters
        ----------
        rand_wall: int[]
            randomly selected wall

        Returns
        -------
        None
        '''
        if rand_wall[0] != 0:
            if (self.maze[rand_wall[0]-1][rand_wall[1]] !=
               self.__path):
                self.maze[rand_wall[0]-1][rand_wall[1]] = \
                        self.__wall
            if ([rand_wall[0]-1, rand_wall[1]] not in
                    self.walls):
                self.walls.\
                    append([rand_wall[0]-1, rand_wall[1]])

    def __remove_complete_wall(self, rand_wall):
        '''
        remove the wall from the not proccessed wall array

        Parameters
        ----------
        rand_wall: int[]
            randomly selected wall

        Returns
        -------
        None
        '''
        for single_wall in self.walls:
            if single_wall[0] == rand_wall[0] and single_wall[1] \
                   == rand_wall[1]:
                self.walls.remove(single_wall)

    def draw_maze(self):
        '''
        draw the grid to the console

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        for height in range(0, self.maze_size):
            for width in range(0, self.maze_size):
                if self.maze[height][width] == self.__path:
                    print(Fore.BLACK + Back.BLACK +
                          f"{self.maze[height][width]} ", end="")
                elif self.maze[height][width] == self.__solution:
                    print(Fore.GREEN + Back.GREEN +
                          f"{self.maze[height][width]} ", end="")
                elif self.maze[height][width] == self.__user_move:
                    if (height == self.solver_current[0]
                       and width == self.solver_current[1]):
                        print(Fore.BLUE + Back.CYAN +
                              f"{self.maze[height][width]} ", end="")
                    else:
                        print(Fore.BLUE + Back.BLUE +
                              f"{self.maze[height][width]} ", end="")
                else:
                    print(Fore.WHITE + Back.WHITE +
                          f"{self.maze[height][width]} ",
                          end="")
            print()

    def __surrounding_cells(self, rand_wall):
        '''
        count all paths surrounding the wall

        Parameters
        ----------
        rand_wall: int[]
            randomly selected wall

        Returns
        -------
        s_cells: int
            total of surrounding paths
        '''
        s_cells = 0
        if self.maze[rand_wall[0]-1][rand_wall[1]] == self.__path:
            s_cells += 1
        if self.maze[rand_wall[0]+1][rand_wall[1]] == self.__path:
            s_cells += 1
        if self.maze[rand_wall[0]][rand_wall[1]-1] == self.__path:
            s_cells += 1
        if self.maze[rand_wall[0]][rand_wall[1]+1] == self.__path:
            s_cells += 1
        return s_cells

    def __fill_open_maze_walls(self):
        '''
        fill the open maze items will the wall icons

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        for height in range(0, self.maze_size):
            for width in range(0, self.maze_size):
                if self.maze[height][width] == self.__open:
                    self.maze[height][width] = self.__wall

    def __create_ins_and_outs(self):
        '''
        set the entrance and exit of the maze

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        for width in range(0, self.maze_size):
            if self.maze[1][width] == self.__path:
                self.maze[0][width] = self.__path
                break

        for width in range(self.maze_size-1, 0, -1):
            if self.maze[self.maze_size-2][width] == self.__path:
                self.maze[self.maze_size-1][width] = self.__path
                break

    def solve_maze(self):
        '''
        will find the path to get to the end of the maze and set to path

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        s_and_e = self.__get_start_and_end()
        path = []

        if s_and_e == 0:
            self.__remove_from_maze(self.__solution)
            self.draw_maze()
            print(self.solver_current)
        elif s_and_e == 1:
            print("The maze could not find a start or end")
        else:
            path = self.__create_path(path, s_and_e[0], (), s_and_e[1])
            for step in path:
                self.maze[step[0]][step[1]] = self.__solution
            self.__remove_from_maze(self.__user_move)
            self.draw_maze()
            self.solver_current = None
            print(self.solver_current)

    def __get_start_and_end(self):
        '''
        will find the start and end coordinates so it will start the user
        at the right place in the maze

        Parameters
        ----------
        None

        Returns
        -------
        start_end: int[]
            start coodinates in index 0
            end coordinates in index 1

        0 if the maze has already been solved
        1 if it cannot find a start and end point
        '''
        the_coord = ()
        start_end = []
        for count in range(2):
            if count == 0:
                the_index = 0
            else:
                the_index = self.maze_size - 1

            for width in range(0, self.maze_size):
                if (self.maze[the_index][width] == self.__path or
                   self.maze[the_index][width] == self.__user_move):
                    the_coord = (the_index, width)
                    start_end.append(the_coord)
                    break
                if self.maze[the_index][width] == self.__solution:
                    print("Maze already solved!")
                    return 0
        if len(start_end) < 2:
            print("No start point")
            return 1
        return start_end

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

    def __set_next_path(self, count, current):
        '''
        set the next coordiante that the maze should try to go

        Parameters
        ----------
        count: int
            direction number
            0 = up
            1 = left
            2 = right
            3 = down
        current: int[]
            current position in the maze

        Returns
        -------
        temp_path: int[]
            next positon to go int he maze
        '''
        temp_path = ()
        if count == 0:
            temp_path = (current[0]-1, current[1])
        elif count == 1:
            temp_path = (current[0], current[1]-1)
        elif count == 2:
            temp_path = (current[0], current[1]+1)
        else:
            temp_path = (current[0]+1, current[1])
        return temp_path

    def __remove_from_maze(self, maze_type):
        '''
        find the solution/usermove in the array and change the
        character into the path

        Parameters
        ----------
        maze_type: str
            the item we want to remove from the maze

        Returns
        -------
        None
        '''
        for height in range(0, self.maze_size):
            for width in range(0, self.maze_size):
                if self.maze[height][width] == maze_type:
                    self.maze[height][width] = self.__path

    def save_maze(self):
        '''
        store the maze details to google sheets

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        valid = False
        while valid is False:
            valid = True
            if self.loaded is True:
                SHEET.del_worksheet(SHEET.worksheet(self.maze_name))
            print("Saving maze...")
            try:
                new_sheet = SHEET.add_worksheet(self.maze_name,
                                                self.maze_size + 1,
                                                self.maze_size)
            except Exception:
                print(f"Could not save because: A sheet with the name '"
                      f"{self.maze_name}' already exists.")
                valid = False
                name_valid = False
                while name_valid is False:
                    new_name = input("Please enter a new name for the" +
                                     " sheet \n")
                    name_valid = valid_user_input(new_name)
                self.maze_name = new_name
            else:
                for row in self.maze:
                    new_sheet.append_row(row)
                new_sheet.append_row(self.solver_current)
                if self.loaded is False:
                    saves_worksheet = SHEET.worksheet('saves')
                    saves_worksheet_len = len(saves_worksheet.col_values(1))

                    saves_worksheet.update('A'+str(saves_worksheet_len+1),
                                           self.maze_name)
                print("Maze saved!")
                self.loaded = True
                self.draw_maze()

    def load_in_maze(self, name, matrix, current):
        '''
        update the graph with the data that was loaded from google sheets

        Parameters
        ----------
        name: str
            maze name
        matrix: int[]
            the maze array
        current: int[]
            current postion the solver is at
            None if has not been attempted

        Returns
        -------
        None
        '''
        self.maze_name = name
        self.maze = matrix
        self.maze_size = len(matrix[0])
        self.loaded = True
        self.solver_current = current

    def user_solve_maze(self):
        '''
        using the WASD keys user can solve the maze by drawing a path

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        print()
        s_and_e = self.__get_start_and_end()
        if s_and_e != 0 and s_and_e != 1:
            if self.solver_current is None:
                self.maze[s_and_e[0][0]][s_and_e[0][1]] = self.__user_move
                current = s_and_e[0]
                self.solver_current = current
            else:
                current = self.solver_current
            self.draw_maze()
            print()
            end_solver = False
            while end_solver is False:
                print("Controls: (W - Up, S - Down, D - Right, A - Left) "
                      "then press Enter... Press 0 to Exit")
                command = input("Please enter the direction you want to go\n")
                if command.upper() == "W":
                    print("Move Up")
                    current = self.__set_user_path(command.upper(), current)
                elif command.upper() == "A":
                    print("Move Left")
                    current = self.__set_user_path(command.upper(), current)
                elif command.upper() == "S":
                    print("Move Down")
                    current = self.__set_user_path(command.upper(), current)
                elif command.upper() == "D":
                    print("Move Right")
                    current = self.__set_user_path(command.upper(), current)
                elif command.upper() == "0":
                    print("Exit Solver")
                    end_solver = True
                else:
                    print("Invalid Move")
                self.solver_current = current
                self.draw_maze()
                if current[0] == s_and_e[1][0] and current[1] == s_and_e[1][1]:
                    print("Solved it")
                    end_solver = True
        else:
            self.draw_maze()

    def __set_user_path(self, direction, current):
        '''
        sets the game maze array path to the user move character.
        If the user selects a direction that is blocked by a wall then
        it will give an error message

        Parameters
        ----------
        direction: str
            W,A,S,D
        current: int[]
            current position in the maze

        Returns
        -------
        current: int[]
            the new position in the maze or the orginal
        '''
        if direction == "W":
            text_direction = "up"
            edge_coord = current[0]
            edge_coord_limit = 0
            new_x = current[0]-1
            new_y = current[1]
        elif direction == "D":
            text_direction = "right"
            edge_coord = current[1]
            edge_coord_limit = self.maze_size-1
            new_x = current[0]
            new_y = current[1]+1
        elif direction == "S":
            text_direction = "down"
            edge_coord = current[0]
            edge_coord_limit = self.maze_size-1
            new_x = current[0]+1
            new_y = current[1]
        elif direction == "A":
            text_direction = "left"
            edge_coord = current[1]
            edge_coord_limit = 0
            new_x = current[0]
            new_y = current[1]-1

        if edge_coord == edge_coord_limit:
            print(f"Error border - Cannot go {text_direction}")
            return current
        if self.maze[new_x][new_y] == self.__wall:
            print(f"Error wall - Cannot go {text_direction}")
            return current
        if self.maze[new_x][new_y] == self.__user_move:
            self.maze[current[0]][current[1]] = self.__path
        else:
            self.maze[new_x][new_y] = self.__user_move
        current = [new_x, new_y]
        return current


class GameGraph:
    '''
    Graph Class
    '''
    # class attribute
    graph_nodes = []
    graph_node_names = []
    loaded = False

    def __init__(self, name):
        # instance attribute
        self.graph_name = name
        self.graph_nodes = []
        self.graph_node_names = []
        self.loaded = False

    def add_node_to_graph(self):
        '''
        This will add the node to the graph array and add a
        new array item to all items in the array
        '''
        name = input("Please enter the name of the node:\n")
        name_in_array = self.get_node_index(name)
        if name_in_array == -1:
            self.graph_node_names.append(name)
            temp_array = []
            for _ in self.graph_node_names:
                temp_array.append(0)
            self.graph_nodes.append(temp_array)
            for none in range(len(self.graph_nodes)-1):
                self.graph_nodes[none].append(0)
        else:
            print(f"{name} is already in the graph!")

    def add_link_to_graph(self, mode):
        '''
        will change the value in the graph array to represent a new link
        between nodes
        '''
        print(f"{mode} the link between nodes")
        first_name = input("Please enter the name of the first node:\n")
        first_name_index = self.get_node_index(first_name)
        if first_name_index != -1:
            second_name = input("Please enter the name of the second node:\n")
            second_name_index = self.get_node_index(second_name)
            if second_name_index != -1:
                if first_name_index != second_name_index:
                    print(f"{mode} link between "
                          f"{self.graph_node_names[first_name_index]} "
                          f" to {self.graph_node_names[second_name_index]}")
                    if mode == "Delete":
                        link_weight = 0
                    else:
                        link_weight = get_number_option("node weight", 0, 100)
                    self.graph_nodes[first_name_index][second_name_index] = \
                        link_weight
                    self.graph_nodes[second_name_index][first_name_index] = \
                        link_weight
                    print(f"Link Change Complete - "
                          f"{self.graph_node_names[first_name_index]} to "
                          f"{self.graph_node_names[second_name_index]} "
                          f"weight {link_weight}")
                else:
                    print("Error: Cannot change link node to itself")
            else:
                print("Error: Name not found in graph")
        else:
            print("Error: Name not found in graph")

    def get_node_index(self, search_string):
        '''
        Will iterate through the array to see what the index is of the
        string that is passed to it. If the string is not in the array
        it will return -1
        '''
        for name in self.graph_node_names:
            if name.upper() == search_string.upper():
                return self.graph_node_names.index(name)
        return -1

    def show_graph_status(self):
        '''
        will output all the values linked to the graph
        '''
        print("Graph name: " + self.graph_name)
        print([str(i) + " = " + self.graph_node_names[i]
              for i in range(len(self.graph_node_names))])
        count = 0
        for node in self.graph_nodes:
            print(str(count) + " " + str(node))
            count = count + 1

    def quick_fill_graph(self):
        '''
        Will put set values into the graph to allow the user to see an example
        graph
        '''
        self.graph_node_names = ["Zero", "One", "Two", "Three", "Four", "Five",
                                 "six", "seven", "eight"]
        self.graph_nodes = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                            [4, 0, 8, 0, 0, 0, 0, 11, 0],
                            [0, 8, 0, 7, 0, 4, 0, 0, 2],
                            [0, 0, 7, 0, 9, 14, 0, 0, 0],
                            [0, 0, 0, 9, 0, 10, 0, 0, 0],
                            [0, 0, 4, 14, 10, 0, 2, 0, 0],
                            [0, 0, 0, 0, 0, 2, 0, 1, 6],
                            [8, 11, 0, 0, 0, 0, 1, 0, 7],
                            [0, 0, 2, 0, 0, 0, 6, 7, 0]
                            ]

    def delete_node(self):
        '''
        Delete a node from the graph array.
        '''
        print("Delete node")
        node_name = input("Please enter the name of the node:\n")
        node_name_index = self.get_node_index(node_name)
        if node_name_index != -1:
            count = len(self.graph_nodes)
            for node_index in range(count):
                del self.graph_nodes[node_index][node_name_index]
            del self.graph_node_names[node_name_index]
            del self.graph_nodes[node_name_index]
        else:
            print("Error: Name not found in graph")

    def show_connections(self):
        '''
        Show all the connections for one of the nodes
        '''
        print("Show connected nodes")
        node_name = input("Please enter the name of the node:\n")
        node_name_index = self.get_node_index(node_name)
        if node_name_index != -1:
            has_link = False
            for index, node in enumerate(self.graph_nodes[node_name_index]):
                if node != 0:
                    has_link = True
                    print(f"{self.graph_node_names[node_name_index]} to "
                          f"{self.graph_node_names[index]} -- weight: "
                          f"{self.graph_nodes[node_name_index][index]}")
            if has_link is False:
                print(f"{self.graph_node_names[node_name_index]} has no "
                      f"links to other nodes")
        else:
            print("Error: Name not found in graph")

    def dijkstra_path(self):
        '''
        Find the shortest path to a node
        '''
        start_name = input("Please enter the name of the start node:\n")
        start_name_index = self.get_node_index(start_name)
        if start_name_index != -1:
            end_name = input("Please enter the name of the "
                             "destination node:\n")
            end_name_index = self.get_node_index(end_name)
            if end_name_index != -1:

                total_distance = [sys.maxsize] * len(self.graph_node_names)
                previous_node = [None] * len(self.graph_node_names)
                total_distance[start_name_index] = 0
                visited = [False]*len(self.graph_node_names)

                for _ in range(len(self.graph_node_names)):
                    min_number = sys.maxsize

                    for node in range(len(self.graph_node_names)):
                        if total_distance[node] < min_number and \
                                visited[node] is False:
                            min_number = total_distance[node]
                            min_index = node
                    current_node = min_index

                    visited[current_node] = True

                    for node in range(len(self.graph_node_names)):
                        if self.graph_nodes[current_node][node] > 0 and \
                            visited[node] is False and \
                            total_distance[node] > \
                                total_distance[current_node] + \
                                self.graph_nodes[current_node][node]:
                            total_distance[node] = \
                                total_distance[current_node] + \
                                self.graph_nodes[current_node][node]
                            previous_node[node] = current_node
                self.print_short_path(total_distance, previous_node,
                                      start_name_index, end_name_index,
                                      visited[end_name_index])

            else:
                print("Error: Name not found in graph")
        else:
            print("Error: Name not found in graph")

    def print_short_path(self, total_distance, previous_node, start_index,
                         end_index, reachable):
        '''
        Will write out the instructions on how to follow the shortest path
        '''
        print()
        if reachable is True:
            print(f"{self.graph_node_names[start_index]} to "
                  f"{self.graph_node_names[end_index]} has "
                  f"weight of {total_distance[end_index]} "
                  )
            the_node = end_index
            print("The steps to destination")
            solution = []
            solution_name = []
            while the_node != start_index:
                solution.insert(0, the_node)
                solution_name.insert(0, self.graph_node_names[the_node])
                the_node = previous_node[the_node]
            solution_name.insert(0, self.graph_node_names[start_index])
            print(solution_name)
            last_node = start_index

            for index, node in enumerate(solution):
                print(f"{index+1}) {self.graph_node_names[last_node]} to "
                      f"{self.graph_node_names[node]} ("
                      f"weight = {self.graph_nodes[last_node][node]})")
                last_node = node
        else:
            print(f"There is no route between "
                  f"{self.graph_node_names[start_index]} and "
                  f"{self.graph_node_names[end_index]}")

    def load_in_graph(self, name, node_names, matrix):
        '''
        Will update the graph with the data that was loaded from google sheets
        '''
        self.graph_name = name
        self.graph_node_names = node_names
        self.graph_nodes = matrix
        self.loaded = True

    def save_graph(self):
        '''
        Will store the maze details to sheets
        '''
        valid = False
        while valid is False:
            valid = True
            if self.loaded is True:
                SHEET.del_worksheet(SHEET.worksheet(self.graph_name))
            print("Saving maze...")
            try:
                new_sheet = SHEET.add_worksheet(self.graph_name,
                                                len(self.graph_node_names) + 1,
                                                len(self.graph_node_names))
            except Exception:
                print(f"Could not save because: A sheet with the name '"
                      f"{self.graph_name}' already exists.")
                valid = False
                name_valid = False
                while name_valid is False:
                    new_name = input("Please enter a new name for the" +
                                     " sheet \n")
                    name_valid = valid_user_input(new_name)
                self.graph_name = new_name
            else:
                new_sheet.append_row(self.graph_node_names)
                for row in self.graph_nodes:
                    new_sheet.append_row(row)
                if self.loaded is False:
                    saves_worksheet = SHEET.worksheet('saves')
                    saves_worksheet_len = len(saves_worksheet.col_values(2))

                    saves_worksheet.update('B'+str(saves_worksheet_len+1),
                                           self.graph_name)
                print("Graph saved!")
                self.loaded = True


def show_menu():
    '''
    Will show the main menu to the console
    '''
    print("--- Menu ---")
    print("1) Create Maze")
    print("2) Create Graph")
    print("3) Load Maze from file")
    print("4) Load Graph from file")
    print("0) Exit")
    print(("===================="))


def show_maze_menu():
    '''
    Will show the menu for the maze to the console
    '''
    print()
    print("--- Maze Menu ---")
    print("1) Solve/ Unsolve Maze")
    print("2) Save maze to file")
    print("3) User Solve Maze")
    print("0) Back to Main menu")
    print(("===================="))


def show_graph_menu():
    '''
    Will show the menu for the graph to the console
    '''
    print()
    print("--- Graph Menu ---")
    print("1) Add Node")
    print("2) Add Link")
    print("3) Delete Link")
    print("4) Delete Node")
    print("5) Save Graph")
    print("6) Show Graph Details")
    print("7) Fill With Sample Data")
    print("8) Show Connections for Node")
    print("9) Find Shortest Route")
    print("0) Back to Main menu")
    print(("===================="))


def main():
    '''
    Main, the program start
    '''
    # show_app_title()
    # print("Welcome to Route me the best way to find the quickest route.\n")
    # show_menu()
    menu_option = None
    while menu_option != 0:
        if menu_option == 1:
            menu_option_1(None)
        elif menu_option == 2:
            menu_option_2(None)
        elif menu_option == 3:
            get_saved_file_names(1)
        elif menu_option == 4:
            get_saved_file_names(2)
        show_app_title()
        show_menu()
        menu_option = get_number_option("menu", 0, 4)


def menu_option_1(the_maze=None):
    '''
    get the user input and perform the method the user selects for the maze
    '''
    if the_maze is None:
        the_maze = None
        name_valid = False
        while name_valid is False:
            maze_name = input("Please enter the name of the maze:\n")
            name_valid = valid_user_input(maze_name)
        maze_size = get_number_option("maze size", 10, 40)
        the_maze = GameMaze(maze_size, maze_name)
    the_maze.draw_maze()
    show_maze_menu()
    maze_menu_option = get_number_option("maze menu", 0, 3)
    while maze_menu_option != 0:
        if maze_menu_option == 1:
            the_maze.solve_maze()
        elif maze_menu_option == 2:
            the_maze.save_maze()
        elif maze_menu_option == 3:
            the_maze.user_solve_maze()
        show_maze_menu()
        maze_menu_option = get_number_option("maze menu", 0, 3)
    the_maze = None


def menu_option_2(the_graph=None):
    '''
    get the user input and perform the method the user selects for the graph
    '''
    if the_graph is None:
        name_valid = False
        while name_valid is False:
            graph_name = input("Please enter the name of the graph:\n")
            name_valid = valid_user_input(graph_name)
        the_graph = GameGraph(graph_name)
    show_graph_menu()
    graph_menu_option = get_number_option("graph menu", 0, 9)
    while graph_menu_option != 0:
        if graph_menu_option == 1:
            the_graph.add_node_to_graph()
        elif graph_menu_option == 2:
            the_graph.add_link_to_graph("Add / Edit")
        elif graph_menu_option == 3:
            the_graph.add_link_to_graph("Delete")
        elif graph_menu_option == 4:
            the_graph.delete_node()
        elif graph_menu_option == 5:
            the_graph.save_graph()
        elif graph_menu_option == 6:
            the_graph.show_graph_status()
        elif graph_menu_option == 7:
            the_graph.quick_fill_graph()
        elif graph_menu_option == 8:
            the_graph.show_connections()
        elif graph_menu_option == 9:
            the_graph.dijkstra_path()
        show_graph_menu()
        graph_menu_option = get_number_option("graph menu", 0, 9)
    the_graph = None


def get_number_option(name, start, end):
    '''
    Will get the user to enter a number and will validate their entry
    '''
    invalid_option = True
    while invalid_option:
        try:
            invalid_option = True
            menu_option = int(input(f"Please enter your {name} "
                                    f"choice ({start} - {end}):\n"))
        except ValueError:
            print(f"Not a valid number - Please enter a number between "
                  f"{start} and {end}")
        else:
            if menu_option >= start and menu_option <= end:
                invalid_option = False
            else:
                print(f'Number option not avaliable - Please enter a '
                      f'number between {start} and {end}')
    return menu_option


def valid_user_input(text):
    '''
    Will validate the user input to make sure it starst with a letter
    '''
    if len(text) < 1:
        print("Input is not long enough")
        return False
    elif re.search("^[a-zA-Z]", text) is None:
        print("Input must start with a letter")
        return False
    else:
        return True


def show_app_title():
    '''
    Will show the Title logo for the route me app
    '''
    print(Fore.BLUE + Back.WHITE +
          "==============================================")
    print(Fore.BLUE + Back.WHITE +
          "______            _             ___  ___      ")
    print(Fore.BLUE + Back.WHITE +
          "| ___ \          | |            |  \/  |      ")
    print(Fore.BLUE + Back.WHITE +
          "| |_/ /___  _   _| |_ ___ ______| .  . | ___  ")
    print(Fore.BLUE + Back.WHITE +
          '|    // _ \| | | | __/ _ \______| |\/| |/ _ \ ')
    print(Fore.BLUE + Back.WHITE +
          "| |\ \ (_) | |_| | ||  __/      | |  | |  __/ ")
    print(Fore.BLUE + Back.WHITE +
          "\_| \_\___/ \__,_|\__\___|      \_|  |_/\___| ")
    print(Fore.BLUE + Back.WHITE +
          "==============================================")
    print()
    print("Welcome to Route-me the best way to find the quickest route.\n")


def get_saved_file_names(save_type):
    '''
    Will show the user all the graphs and mazes that are saved and will
    allow the user o enter the worksheets name to load it
    '''
    saved_sheets = SHEET.worksheet('saves')
    saved_names = saved_sheets.col_values(save_type)
    if len(saved_names) != 0:
        print("Files available to load:")
        print("========================")
        for name in saved_names:
            print(name)
        print()
        file_name_enetered = input("Please enter the file name you want " +
                                   "to open (case sensitive) \n")
        if file_name_enetered in saved_names:
            if save_type == 1:
                print("Maze loading...")
                load_maze(file_name_enetered)
            elif save_type == 2:
                print("Graph loading...")
                load_graph(file_name_enetered)
        else:
            print("This sheet could not be found!")
    else:
        print("No saved sheets")


def load_graph(sheet_name):
    '''
    Loads the data from the sheet and will create a new instance of graph
    with the data
    '''
    temp_graph = SHEET.worksheet(sheet_name)
    temp_graph_name = sheet_name
    temp_graph_node_names = temp_graph.row_values(1)
    temp_graph_node = temp_graph.get_all_values()
    temp_graph_node.pop(0)
    int_temp_graph_node = []
    the_graph = None

    for row in temp_graph_node:
        int_row = [int(num) for num in row]
        int_temp_graph_node.append(int_row)

    the_graph = GameGraph(temp_graph_name)
    the_graph.load_in_graph(temp_graph_name, temp_graph_node_names,
                            int_temp_graph_node)

    menu_option_2(the_graph)


def load_maze(sheet_name):
    '''
    Loads the data from the sheet and will create a new instance of maze
    with the data
    '''
    the_maze = None
    temp_maze = SHEET.worksheet(sheet_name).get_all_values()
    temp_maze_name = sheet_name
    temp_maze_size = len(temp_maze[0])
    current = None

    the_maze = GameMaze(temp_maze_size, temp_maze_name)
    if len(temp_maze) != len(temp_maze[0]):
        current = temp_maze.pop()
        current = [int(current[0]), int(current[1])]

    the_maze.load_in_maze(temp_maze_name, temp_maze, current)
    menu_option_1(the_maze)


main()
