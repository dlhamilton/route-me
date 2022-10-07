# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint
import random
from colorama import init, Fore, Back, Style


class Game_maze:
    '''
    Maze Class
    '''
    # class attribute
    path = 'p'
    wall = 'w'
    open = "O"
    walls = []
    maze = []

    def __init__(self, maze_size):
        # instance attribute
        self.maze_size = maze_size
        self.create_blank_maze()
        starting_maze_generation_position_h = self.starting_maze_generation_position(self.maze_size)
        starting_maze_generation_position_w = self.starting_maze_generation_position(self.maze_size)
        self.maze[starting_maze_generation_position_h][starting_maze_generation_position_w] = self.path
        self.get_starting_walls(starting_maze_generation_position_h, starting_maze_generation_position_w)
        self.set_starting_walls(starting_maze_generation_position_h, starting_maze_generation_position_w)
        self.make_maze_walls(maze_size, maze_size)
        
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
        Get the starting posiiton for maze creation but stays away from the edge of the maze"
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
        Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
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
                if self.maze[rand_wall[0]][rand_wall[1]-1] == self.open and self.maze[rand_wall[0]][rand_wall[1]+1] == self.path:

                    surrounding_cell_count = self.surroundingCells(self.maze, rand_wall)
                    if surrounding_cell_count < 2:

                        self.maze[rand_wall[0]][rand_wall[1]] = self.path

                        # Make the walls
                        # The top wall
                        if rand_wall[0] != 0:
                            if self.maze[rand_wall[0]-1][rand_wall[1]] != self.path:
                                self.maze[rand_wall[0]-1][rand_wall[1]] = self.wall
                            if ([rand_wall[0]-1, rand_wall[1]] not in self.walls):
                                self.walls.append([rand_wall[0]-1, rand_wall[1]])

                        # Bottom wall
                        if (rand_wall[0] != height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != self.path):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = self.wall
                            if ([rand_wall[0]+1, rand_wall[1]] not in self.walls):
                                self.walls.append([rand_wall[0]+1, rand_wall[1]])

                        # left wall
                        if (rand_wall[1] != 0):	
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = self.wall
                            if ([rand_wall[0], rand_wall[1]-1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]-1])

                    # Delete wall
                    for single_wall in self.walls:
                        if (single_wall[0] == rand_wall[0] and single_wall[1] == rand_wall[1]):
                            self.walls.remove(single_wall)
                    continue

            # Check if it is a top wall
            if rand_wall[0] != 0:
                if self.maze[rand_wall[0]-1][rand_wall[1]] == self.open and self.maze[rand_wall[0]+1][rand_wall[1]] == self.path:

                    surrounding_cell_count = self.surroundingCells(self.maze, rand_wall)
                    if surrounding_cell_count < 2:

                        self.maze[rand_wall[0]][rand_wall[1]] = self.path

                        # Make the walls
                        # top wall
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != self.path):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = self.wall
                            if ([rand_wall[0]-1, rand_wall[1]] not in self.walls):
                                self.walls.append([rand_wall[0]-1, rand_wall[1]])

                        # left wall
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = self.wall
                            if ([rand_wall[0], rand_wall[1]-1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]-1])

                        # right wall
                        if (rand_wall[1] != width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = self.wall
                            if ([rand_wall[0], rand_wall[1]+1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]+1])

                    # Delete wall
                    for single_wall in self.walls:
                        if (single_wall[0] == rand_wall[0] and single_wall[1] == rand_wall[1]):
                            self.walls.remove(single_wall)
                    continue

            # Check if it is a bottom wall
            if rand_wall[0] != height - 1:
                if self.maze[rand_wall[0]+1][rand_wall[1]] == self.open and self.maze[rand_wall[0]-1][rand_wall[1]] == self.path:

                    surrounding_cell_count = self.surroundingCells(self.maze, rand_wall)
                    if surrounding_cell_count < 2:

                        self.maze[rand_wall[0]][rand_wall[1]] = self.path

                        # Make the walls
                        # bottom wall
                        if (rand_wall[0] != height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != self.path):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = self.wall
                            if ([rand_wall[0]+1, rand_wall[1]] not in self.walls):
                                self.walls.append([rand_wall[0]+1, rand_wall[1]])

                        # left wall
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = self.wall
                            if ([rand_wall[0], rand_wall[1]-1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]-1])

                        # right wall
                        if (rand_wall[1] != width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = self.wall
                            if ([rand_wall[0], rand_wall[1]+1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]+1])

                    # Delete wall
                    for single_wall in self.walls:
                        if (single_wall[0] == rand_wall[0] and single_wall[1] == rand_wall[1]):
                            self.walls.remove(single_wall)
                    continue


            # Check if it is a right wall
            if rand_wall[1] != width-1:
                if self.maze[rand_wall[0]][rand_wall[1]+1] == self.open and self.maze[rand_wall[0]][rand_wall[1]-1] == self.path:

                    surrounding_cell_count = self.surroundingCells(self.maze, rand_wall)
                    if surrounding_cell_count < 2:

                        self.maze[rand_wall[0]][rand_wall[1]] = self.path

                        # Make the walls
                        # right wall
                        if (rand_wall[1] != width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != self.path):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = self.wall
                            if ([rand_wall[0], rand_wall[1]+1] not in self.walls):
                                self.walls.append([rand_wall[0], rand_wall[1]+1])

                        # bottom wall
                        if (rand_wall[0] != height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != self.path):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = self.wall
                            if ([rand_wall[0]+1, rand_wall[1]] not in self.walls):
                                self.walls.append([rand_wall[0]+1, rand_wall[1]])

                        # top wall
                        if rand_wall[0] != 0:	
                            if self.maze[rand_wall[0]-1][rand_wall[1]] != self.path:
                                self.maze[rand_wall[0]-1][rand_wall[1]] = self.wall
                            if [rand_wall[0]-1, rand_wall[1]] not in self.walls:
                                self.walls.append([rand_wall[0]-1, rand_wall[1]])

            # Delete wall
            for single_wall in self.walls:
                if (single_wall[0] == rand_wall[0] and single_wall[1] == rand_wall[1]):
                    self.walls.remove(single_wall)
            continue

    def draw_maze(self):
        '''
        Draw the grid to the console
        '''
        for h in range(0, self.maze_size):
            for w in range(0, self.maze_size):
                print(f"{self.maze[h][w]} ", end="")
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


def show_menu():
    print("--- Menu ---")
    print("1) Create random maze")
    print("2) Solve Maze")
    print("3) Create custom maze")
    print("4) Load maze from file")
    print("5) Save maze to file")
    print("6) Exit")


def main():
    print("----------")
    print("Route Me")
    print("----------")
    print("Welcome to Route me the best way to find the quickest route.\n")
    show_menu()


main()
TheMaze = Game_maze(20)
TheMaze.draw_maze()