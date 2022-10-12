'''
route-me
'''
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# from pprint import pprint
# # Library for INT_MAX
import sys
import random
from colorama import init, Fore, Back
init(autoreset=True)


class GameMaze:
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
        for _ in range(0, height):
            row = []
            for _ in range(0, width):
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
                        self.surrounding_cells(self.maze, rand_wall)
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
                        if rand_wall[0] != height-1:
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] !=
                                    self.path):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = \
                                    self.wall
                            if ([rand_wall[0]+1, rand_wall[1]] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0]+1, rand_wall[1]])

                        # left wall
                        if rand_wall[1] != 0:
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
                        self.surrounding_cells(self.maze, rand_wall)
                    if surrounding_cell_count < 2:

                        self.maze[rand_wall[0]][rand_wall[1]] = self.path

                        # Make the walls
                        # top wall
                        if rand_wall[0] != 0:
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] !=
                                    self.path):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = \
                                    self.wall
                            if ([rand_wall[0]-1, rand_wall[1]] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0]-1, rand_wall[1]])

                        # left wall
                        if rand_wall[1] != 0:
                            if (self.maze[rand_wall[0]][rand_wall[1]-1]
                                    != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = \
                                    self.wall
                            if ([rand_wall[0], rand_wall[1]-1] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0], rand_wall[1]-1])

                        # right wall
                        if rand_wall[1] != width-1:
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
                        self.surrounding_cells(self.maze, rand_wall)
                    if surrounding_cell_count < 2:

                        self.maze[rand_wall[0]][rand_wall[1]] = self.path

                        # Make the walls
                        # bottom wall
                        if rand_wall[0] != height-1:
                            if (self.maze[rand_wall[0]+1][rand_wall[1]]
                                    != self.path):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = \
                                    self.wall
                            if ([rand_wall[0]+1, rand_wall[1]] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0]+1, rand_wall[1]])

                        # left wall
                        if rand_wall[1] != 0:
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] !=
                                    self.path):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = \
                                    self.wall
                            if ([rand_wall[0], rand_wall[1]-1] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0], rand_wall[1]-1])

                        # right wall
                        if rand_wall[1] != width-1:
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
                        self.surrounding_cells(self.maze, rand_wall)
                    if surrounding_cell_count < 2:

                        self.maze[rand_wall[0]][rand_wall[1]] = self.path

                        # Make the walls
                        # right wall
                        if rand_wall[1] != width-1:
                            if (self.maze[rand_wall[0]][rand_wall[1]+1]
                                    != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = \
                                    self.wall
                            if ([rand_wall[0], rand_wall[1]+1] not in
                                    self.walls):
                                self.walls.\
                                    append([rand_wall[0], rand_wall[1]+1])

                        # bottom wall
                        if rand_wall[0] != height-1:
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
        for height in range(0, self.maze_size):
            for width in range(0, self.maze_size):
                if self.maze[height][width] == self.path:
                    print(Fore.BLACK + f"{self.maze[height][width]} ", end="")
                elif self.maze[height][width] == self.solution:
                    print(Fore.GREEN + f"{self.maze[height][width]} ", end="")
                else:
                    print(Fore.WHITE + Back.WHITE +
                          f"{self.maze[height][width]} ",
                          end="")
            print()

    def surrounding_cells(self, maze, rand_wall):
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
        for height in range(0, self.maze_size):
            for width in range(0, self.maze_size):
                if self.maze[height][width] == self.open:
                    self.maze[height][width] = self.wall

    def create_ins_and_outs(self):
        '''
        Set the entrance and exit of the maze
        '''
        for width in range(0, self.maze_size):
            if self.maze[1][width] == self.path:
                self.maze[0][width] = self.path
                break

        for width in range(self.maze_size-1, 0, -1):
            if self.maze[self.maze_size-2][width] == self.path:
                self.maze[self.maze_size-1][width] = self.path
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
        for width in range(0, self.maze_size):
            if self.maze[0][width] == self.path:
                start = width
                current = (0, width)
            if self.maze[0][width] == self.solution:
                return 0
        for width in range(0, self.maze_size):
            if self.maze[self.maze_size - 1][width] == self.path:
                end = width
                goal = (self.maze_size - 1, width)
            if self.maze[self.maze_size - 1][width] == self.solution:
                return 0
        if start is None or end is None:
            print("No start point")
            return 1
        path = self.create_path(path, current, (), goal)
        return path

    def create_path(self, path, current, last, goal):
        '''
        a recursive method to find a path to the exit point in the
        maze returning the path it took.
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
                        temp_path = self.create_path([], next_path, current,
                                                     goal)
                        if len(temp_path) > len(new_path):
                            new_path = temp_path
                            new_path.append(current)

        return new_path

    def add_solution_to_maze(self, path):
        '''
        will take the coordinates of the path and will add them to the maze
        array
        '''
        for step in path:
            self.maze[step[0]][step[1]] = self.solution

    def remove_solution_from_maze(self):
        '''
        will find the solution in the array and change the character into the
        path
        '''
        for height in range(0, self.maze_size):
            for width in range(0, self.maze_size):
                if self.maze[height][width] == self.solution:
                    self.maze[height][width] = self.path


class GameGraph:
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
        print(self.graph_name)
        print(self.graph_node_names)
        for node in self.graph_nodes:
            print(node)

    def quick_fill_graph(self):
        '''
        Will put set values into the graph to allow testing
        self.graph_node_names = ["One", "Two", "Three", "Four", "Five"]
        self.graph_nodes = [[0, 2, 0, 4, 0],
                            [2, 0, 3, 6, 3],
                            [0, 3, 0, 0, 3],
                            [4, 6, 0, 0, 1],
                            [0, 3, 3, 1, 0]]
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
            for index, node in enumerate(self.graph_nodes[node_name_index]):
                if node != 0:
                    print(f"{self.graph_node_names[node_name_index]} to "
                          f"{self.graph_node_names[index]} -- weight: "
                          f"{self.graph_nodes[node_name_index][index]}")
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
                                      start_name_index, end_name_index)

            else:
                print("Error: Name not found in graph")
        else:
            print("Error: Name not found in graph")

    def print_short_path(self, total_distance, previous_node, start_index,
                         end_index):
        '''
        Will write out the instructions on how to follow the shortest path
        '''
        print()
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


def show_menu():
    '''
    Will show the main menu to the console
    '''
    print()
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
    print("0) Back to menu")
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
    print("8) Show Connections")
    print("9) Find Shortest Route")
    print("0) Back to menu")
    print(("===================="))


def main():
    '''
    Main, the program start
    '''
    print("----------")
    print("Route Me")
    print("----------")
    print("Welcome to Route me the best way to find the quickest route.\n")
    show_menu()
    menu_option = get_number_option("menu", 0, 4)
    while menu_option != 0:
        if menu_option == 1:
            menu_option_1()
        elif menu_option == 2:
            menu_option_2()
        show_menu()
        menu_option = get_number_option("menu", 0, 4)


def menu_option_1():
    '''
    get the user input and perform the method the user selects for the maze
    '''
    the_maze = None
    maze_size = get_number_option("maze size", 10, 100)
    the_maze = GameMaze(maze_size)
    the_maze.draw_maze()
    show_maze_menu()
    maze_menu_option = get_number_option("maze menu", 0, 2)
    while maze_menu_option != 0:
        if maze_menu_option == 1:
            the_maze.solve_maze()
        show_maze_menu()
        maze_menu_option = get_number_option("maze menu", 0, 2)


def menu_option_2():
    '''
    get the user input and perform the method the user selects for the graph
    '''
    the_graph = None
    graph_name = input("Please enter the name of the graph:\n")
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
            print("Save goes here")
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


main()
