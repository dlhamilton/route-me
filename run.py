# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint
import random
from colorama import init, Fore, Back, Style
init(autoreset=True)


class Game_maze:
    '''
    Maze Class
    '''
    # class attribute
    path = 'P'
    wall = 'W'
    open = "O"
    solution = "A"
    walls = []
    maze = []

    def __init__(self, maze_size):
        # instance attribute
        self.walls = []
        self.maze = []
        self.maze_size = maze_size
        self.create_blank_maze()
        start_pos_h = \
            self.starting_maze_generation_position(self.maze_size)
        start_pos_w = \
            self.starting_maze_generation_position(self.maze_size)
        self.maze[start_pos_h][start_pos_w] = self.path
        self.get_starting_walls(start_pos_h, start_pos_w)
        self.set_starting_walls(start_pos_h, start_pos_w)
        self.make_maze_walls(maze_size, maze_size)
        self.fill_open_maze_walls()
        self.create_ins_and_outs()

    def create_blank_maze(self):
        """
        creates a 2d array which stores the width and height of the maze
        """
        width = self.maze_size
        height = self.maze_size
        for h in range(0, height):
            row = []
            for w in range(0, width):
                row.append(self.open)
            self.maze.append(row)

    def starting_maze_generation_position(self, max_number):
        '''
        Get the starting posiiton for maze creation but stays away
        from the edge of the maze"
        '''
        starting_pos = int(random.random() * max_number)
        if starting_pos == 0:
            starting_pos += 1
        if starting_pos == max_number-1:
            starting_pos -= 1
        return starting_pos

    def get_starting_walls(self, start_h, start_w):
        '''
        This will add the walls surrounding the starting path to the walls list
        '''
        self.walls.append([start_h-1, start_w])
        self.walls.append([start_h, start_w-1])
        self.walls.append([start_h, start_w+1])
        self.walls.append([start_h+1, start_w])

    def set_starting_walls(self, start_h, start_w):
        '''
        This will set the display of the maze to show the walls
        '''
        self.maze[start_h-1][start_w] = self.wall
        self.maze[start_h][start_w-1] = self.wall
        self.maze[start_h][start_w+1] = self.wall
        self.maze[start_h+1][start_w] = self.wall

    def make_maze_walls(self, height, width):
        '''
        Prims Algorithm
        While there are walls in the list:
        Pick a random wall from the list. If only one of the two cells that
        the wall divides is visited, then:
        Make the wall a passage and mark the unvisited cell as part of the maze
        Add the neighboring walls of the cell to the wall list.
        Remove the wall from the list
        '''
        surrounding_cell_count = 0
        while self.walls:
            # Pick a random wall
            rand_wall = self.walls[int(random.random()*len(self.walls))-1]

            # Check if it is a left wall
            if rand_wall[1] != 0:
                if self.maze[rand_wall[0]][rand_wall[1]-1] == self.open and \
                      self.maze[rand_wall[0]][rand_wall[1]+1] == self.path:

                    surrounding_cell_count = \
                        self.surroundingCells(self.maze, rand_wall)
                    if surrounding_cell_count < 2:

                        self.maze[rand_wall[0]][rand_wall[1]] = self.path

                        # Make the walls
                        # The top wall
                        if rand_wall[0] != 0:
                            if self.maze[rand_wall[0]-1][rand_wall[1]] != \
                                   self.path:
                                self.maze[rand_wall[0]-1][rand_wall[1]] = \
                                    self.wall
                            if [rand_wall[0]-1, rand_wall[1]] \
                                    not in self.walls:
                                self.walls.\
                                    append([rand_wall[0]-1, rand_wall[1]])

                        # Bottom wall
                        if (rand_wall[0] != height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] !=
                                    self.path):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = \
                                    self.wall
                            if ([rand_wall[0]+1, rand_wall[1]] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0]+1, rand_wall[1]])

                        # left wall
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] !=
                                    self.path):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = \
                                    self.wall
                            if ([rand_wall[0], rand_wall[1]-1] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0], rand_wall[1]-1])

                    # Delete wall
                    for single_wall in self.walls:
                        if (single_wall[0] == rand_wall[0] and single_wall[1]
                                == rand_wall[1]):
                            self.walls.remove(single_wall)
                    continue

            # Check if it is a top wall
            if rand_wall[0] != 0:
                if self.maze[rand_wall[0]-1][rand_wall[1]] == self.open and \
                        self.maze[rand_wall[0]+1][rand_wall[1]] == self.path:

                    surrounding_cell_count = \
                        self.surroundingCells(self.maze, rand_wall)
                    if surrounding_cell_count < 2:

                        self.maze[rand_wall[0]][rand_wall[1]] = self.path

                        # Make the walls
                        # top wall
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] !=
                                    self.path):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = \
                                    self.wall
                            if ([rand_wall[0]-1, rand_wall[1]] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0]-1, rand_wall[1]])

                        # left wall
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1]
                                    != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = \
                                    self.wall
                            if ([rand_wall[0], rand_wall[1]-1] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0], rand_wall[1]-1])

                        # right wall
                        if (rand_wall[1] != width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1]
                                    != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = \
                                    self.wall
                            if ([rand_wall[0], rand_wall[1]+1] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0], rand_wall[1]+1])

                    # Delete wall
                    for single_wall in self.walls:
                        if (single_wall[0] == rand_wall[0] and single_wall[1]
                                == rand_wall[1]):
                            self.walls.remove(single_wall)
                    continue

            # Check if it is a bottom wall
            if rand_wall[0] != height - 1:
                if self.maze[rand_wall[0]+1][rand_wall[1]] == self.open and \
                        self.maze[rand_wall[0]-1][rand_wall[1]] == self.path:

                    surrounding_cell_count = \
                        self.surroundingCells(self.maze, rand_wall)
                    if surrounding_cell_count < 2:

                        self.maze[rand_wall[0]][rand_wall[1]] = self.path

                        # Make the walls
                        # bottom wall
                        if (rand_wall[0] != height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]]
                                    != self.path):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = \
                                    self.wall
                            if ([rand_wall[0]+1, rand_wall[1]] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0]+1, rand_wall[1]])

                        # left wall
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] !=
                                    self.path):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = \
                                    self.wall
                            if ([rand_wall[0], rand_wall[1]-1] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0], rand_wall[1]-1])

                        # right wall
                        if (rand_wall[1] != width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1]
                                    != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = \
                                    self.wall
                            if ([rand_wall[0], rand_wall[1]+1] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0], rand_wall[1]+1])

                    # Delete wall
                    for single_wall in self.walls:
                        if (single_wall[0] == rand_wall[0] and single_wall[1]
                                == rand_wall[1]):
                            self.walls.remove(single_wall)
                    continue

            # Check if it is a right wall
            if rand_wall[1] != width-1:
                if self.maze[rand_wall[0]][rand_wall[1]+1] == self.open and \
                        self.maze[rand_wall[0]][rand_wall[1]-1] == self.path:

                    surrounding_cell_count = \
                        self.surroundingCells(self.maze, rand_wall)
                    if surrounding_cell_count < 2:

                        self.maze[rand_wall[0]][rand_wall[1]] = self.path

                        # Make the walls
                        # right wall
                        if (rand_wall[1] != width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1]
                                    != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = \
                                    self.wall
                            if ([rand_wall[0], rand_wall[1]+1] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0], rand_wall[1]+1])

                        # bottom wall
                        if (rand_wall[0] != height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]]
                                    != self.path):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = \
                                    self.wall
                            if ([rand_wall[0]+1, rand_wall[1]] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0]+1, rand_wall[1]])

                        # top wall
                        if rand_wall[0] != 0:	
                            if self.maze[rand_wall[0]-1][rand_wall[1]] != \
                                 self.path:
                                self.maze[rand_wall[0]-1][rand_wall[1]] = \
                                    self.wall
                            if ([rand_wall[0]-1, rand_wall[1]] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0]-1, rand_wall[1]])

            # Delete wall
            for single_wall in self.walls:
                if single_wall[0] == rand_wall[0] and single_wall[1] \
                   == rand_wall[1]:
                    self.walls.remove(single_wall)
            continue

    def draw_maze(self):
        '''
        Draw the grid to the console
        '''
        for h in range(0, self.maze_size):
            for w in range(0, self.maze_size):
                if self.maze[h][w] == self.path:
                    print(Fore.BLACK + f"{self.maze[h][w]} ", end="")
                elif self.maze[h][w] == self.solution:
                    print(Fore.GREEN + f"{self.maze[h][w]} ", end="")
                else:
                    print(Fore.WHITE + Back.WHITE + f"{self.maze[h][w]} ",
                                                    end="")
            print()

    def surroundingCells(self, maze, rand_wall):
        '''
        get all paths surrounding the wall
        '''
        s_cells = 0
        if maze[rand_wall[0]-1][rand_wall[1]] == self.path:
            s_cells += 1
        if maze[rand_wall[0]+1][rand_wall[1]] == self.path:
            s_cells += 1
        if maze[rand_wall[0]][rand_wall[1]-1] == self.path:
            s_cells += 1
        if maze[rand_wall[0]][rand_wall[1]+1] == self.path:
            s_cells += 1
        return s_cells

    def fill_open_maze_walls(self):
        '''
        Fills the open maze items will the wall icons
        '''
        for h in range(0, self.maze_size):
            for w in range(0, self.maze_size):
                if self.maze[h][w] == self.open:
                    self.maze[h][w] = self.wall

    def create_ins_and_outs(self):
        '''
        Set the entrance and exit of the maze
        '''
        for w in range(0, self.maze_size):
            if self.maze[1][w] == self.path:
                self.maze[0][w] = self.path
                break

        for w in range(self.maze_size-1, 0, -1):
            if self.maze[self.maze_size-2][w] == self.path:
                self.maze[self.maze_size-1][w] = self.path
                break

    def solve_maze(self):
        '''
        will find the path to get to the end of the maze
        '''
        path = self.get_maze_start()
        if path == 0:
            self.remove_solution_from_maze()
            self.draw_maze()
        elif path == 1:
            print("The maze could not find a start or end")
        else:
            self.add_solution_to_maze(path)
            self.draw_maze()

    def get_maze_start(self):
        '''
        Will find the start and exit point for the maze
        '''
        start = None
        path = []
        end = None
        goal = ()
        for w in range(0, self.maze_size):
            if self.maze[0][w] == self.path:
                start = w
                current = (0, w)
            if self.maze[0][w] == self.solution:
                return 0
        for w in range(0, self.maze_size):
            if self.maze[self.maze_size - 1][w] == self.path:
                end = w
                goal = (self.maze_size - 1, w)
            if self.maze[self.maze_size - 1][w] == self.solution:
                return 0
        if start == None or end == None:
            print("No start point")
            return 1
        path = self.create_path(path, current, (), goal)
        return path

    def create_path(self, path, current, last, goal):
        '''
        a recursive method to find a path to the exit point in the maze returning the path it took.
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
                if count == 0:
                    next_path = (current[0]-1, current[1])
                if count == 1:
                    next_path = (current[0], current[1]-1)
                if count == 2:
                    next_path = (current[0], current[1]+1)
                if count == 3:
                    next_path = (current[0]+1, current[1])
                if next_path != last:
                    if self.maze[next_path[0]][next_path[1]] != self.wall:
                        temp_path = self.create_path([], next_path, current, goal)
                        if len(temp_path) > len(new_path):
                            new_path = temp_path
                            new_path.append(current)

        return new_path

    def add_solution_to_maze(self, path):
        for step in path:
            self.maze[step[0]][step[1]] = self.solution

    def remove_solution_from_maze(self):
        for h in range(0, self.maze_size):
            for w in range(0, self.maze_size):
                if self.maze[h][w] == self.solution:
                    self.maze[h][w] = self.path


class Game_Graph:
    '''
    Graph Class
    '''
    # class attribute
    graph_nodes = []
    graph_node_names = []

    def __init__(self, name):
        # instance attribute
        self.graph_name = name

    def add_node_to_graph(self):
        name = input("Please enter the name of the node:\n")
        self.graph_node_names.append(name)
        temp_array = []
        for i in self.graph_node_names:
            temp_array.append(0)
        self.graph_nodes.append(temp_array)
        for j in range(len(self.graph_nodes)-1):
            self.graph_nodes[j].append(0)

    def add_link_to_graph(self):
        name = input("Please enter the name of the first node:\n")
        self.get_node_index(name)

    def get_node_index(self, search_string):
        print(search_string)
        for name in self.graph_node_names:
            if name.upper() == search_string.upper():
                return self.graph_node_names.index(name)
        return -1

    def show_graph_status(self):
        print(self.graph_name)
        print(self.graph_node_names)
        for node in self.graph_nodes:
            print(node)
    
    def quick_fill_graph(self):
        self.graph_name = "Test Data"
        self.graph_node_names = ["One", "Two", "Three", "Four", "Five"]
        self.graph_nodes = [[0, 2, 0, 4, 0],
                            [2, 0, 3, 6, 3],
                            [0, 3, 0, 0, 3],
                            [4, 6, 0, 0, 1],
                            [0, 3, 3, 1, 0]]


def show_menu():
    print("--- Menu ---")
    print("1) Create Maze")
    print("2) Create Graph")
    print("3) Create custom maze")
    print("4) Load maze from file")
    print("5) Save maze to file")
    print("6) Exit")


def show_maze_menu():
    print("--- Maze Menu ---")
    print("1) Solve/ Unsolve Maze")
    print("2) Save maze to file")
    print("3) Back to menu")


def show_graph_menu():
    print("--- Graph Menu ---")
    print("1) Add Node")
    print("2) Add Link")
    print("3) Show Graph Details")
    print("4) Quick Fill Data")
    print("5) Back to menu")


def main():
    print("----------")
    print("Route Me")
    print("----------")
    print("Welcome to Route me the best way to find the quickest route.\n")
    show_menu()
    menu_option = get_number_option("menu", 1, 6)
    while menu_option != 6:
        if menu_option == 1:
            menu_option_1()
        elif menu_option == 2:
            menu_option_2()
        show_menu()
        menu_option = get_number_option("menu", 1, 6)


def menu_option_1():
    TheMaze = None
    maze_size = get_number_option("maze size", 10, 100)
    TheMaze = Game_maze(maze_size)
    TheMaze.draw_maze()
    show_maze_menu()
    maze_menu_option = get_number_option("maze menu", 1, 3)
    while maze_menu_option != 3:
        if maze_menu_option == 1:
            TheMaze.solve_maze()
        show_maze_menu()
        maze_menu_option = get_number_option("maze menu", 1, 3)


def menu_option_2():
    TheGraph = None
    graph_name = input("Please enter the name of the graph:\n")
    TheGraph = Game_Graph(graph_name)
    show_graph_menu()
    graph_menu_option = get_number_option("graph menu", 1, 5)
    while graph_menu_option != 5:
        if graph_menu_option == 1:
            TheGraph.add_node_to_graph()
        elif graph_menu_option == 2:
            TheGraph.add_link_to_graph()
        elif graph_menu_option == 3:
            TheGraph.show_graph_status()
        elif graph_menu_option == 4:
            TheGraph.quick_fill_graph()
        show_graph_menu()
        graph_menu_option = get_number_option("graph menu", 1, 5)


def get_number_option(name, start, end):
    invalid_option = True
    while invalid_option:
        try:
            invalid_option = True
            menu_option = int(input(f"Please enter your {name} choice ({start} - {end}):\n"))
        except ValueError:
            print(f"Not a valid number - Please enter a number between {start} and {end}")
        except Exception:
            print(f'Another error has occurred - Please enter a number between {start} and {end}')
        else:
            if menu_option >= start and menu_option <= end:
                invalid_option = False
            else:
                print(f'Number option not avaliable - Please enter a number between {start} and {end}')
    return menu_option


main()
