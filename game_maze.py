'''
game maze module for route me

Classes:

    GameMaze

Functions:

    None

Variables:

    None

'''
import random
import gspread
from colorama import init, Fore, Back
from util import (positive_text_color, warning_text_color, negative_text_color,
                  highlight_text_color, heading_text_color, valid_user_input,
                  SHEET, clear_terminal, press_enter)
# reset colour back to default
init(autoreset=True)


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
        elif s_and_e == 1:
            print(negative_text_color("The maze could not find a "
                  " start or end point"))
        else:
            path = self.__create_path(path, s_and_e[0], (), s_and_e[1])
            for step in path:
                self.maze[step[0]][step[1]] = self.__solution
            self.__remove_from_maze(self.__user_move)
            self.solver_current = None

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
                    return 0
        if len(start_end) < 2:
            print(negative_text_color("No start point"))
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
            print(warning_text_color("Saving maze...(Please wait)"))
            try:
                new_sheet = SHEET.add_worksheet(self.maze_name,
                                                self.maze_size + 1,
                                                self.maze_size)
            except gspread.exceptions.APIError:
                print(negative_text_color(
                    f"Could not save because: A sheet with the name '"
                    f"{self.maze_name}' already exists."))
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
                print(positive_text_color("Maze saved!"))
                press_enter()
                self.loaded = True

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
        # s_and_e - start and end coordinates array
        s_and_e = self.__get_start_and_end()
        if s_and_e != 0 and s_and_e != 1:
            if self.solver_current is None:
                self.maze[s_and_e[0][0]][s_and_e[0][1]] = self.__user_move
                current = s_and_e[0]
                self.solver_current = current
            else:
                current = self.solver_current
            clear_terminal()
            self.draw_maze()
            print()
            end_solver = False
            while end_solver is False:
                print(heading_text_color("Controls: (W - Up, S - Down, D - "
                      "Right, A - Left) then press Enter...\nPress 0 to Exit"))
                command = input("Please enter the direction you want to go\n")
                if command.upper() == "W":
                    print(warning_text_color("Moving Up..."))
                    current = self.__set_user_path(command.upper(), current)
                elif command.upper() == "A":
                    print(warning_text_color("Moving Left..."))
                    current = self.__set_user_path(command.upper(), current)
                elif command.upper() == "S":
                    print(warning_text_color("Moving Down..."))
                    current = self.__set_user_path(command.upper(), current)
                elif command.upper() == "D":
                    print(warning_text_color("Moving Right..."))
                    current = self.__set_user_path(command.upper(), current)
                elif command.upper() == "0":
                    print(highlight_text_color("Exit Solver"))
                    press_enter()
                    end_solver = True
                else:
                    print(negative_text_color("Invalid move command!"))
                    press_enter()
                self.solver_current = current
                clear_terminal()
                self.draw_maze()
                if current[0] == s_and_e[1][0] and current[1] == s_and_e[1][1]:
                    print()
                    print(positive_text_color("Solved it"))
                    print()
                    press_enter()
                    end_solver = True
        else:
            if s_and_e == 0:
                print(warning_text_color("Maze already solved!"))
                press_enter()

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
            print(negative_text_color(f"Error border - Cannot go "
                  f"{text_direction}"))
            press_enter()
            return current
        if self.maze[new_x][new_y] == self.__wall:
            print(negative_text_color(f"Error wall - Cannot go "
                  f"{text_direction}"))
            press_enter()
            return current
        if self.maze[new_x][new_y] == self.__user_move:
            self.maze[current[0]][current[1]] = self.__path
        else:
            self.maze[new_x][new_y] = self.__user_move
        current = [new_x, new_y]
        print(positive_text_color("Move complete!"))
        return current
