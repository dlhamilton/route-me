# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint
import random

path = 'p'
wall = 'w'
open = "O"


def create_maze():
    '''
    build a random maze
    '''
    maze = create_blank_maze()
    starting_maze_generation_position_h = starting_maze_generation_position(10)
    starting_maze_generation_position_w = starting_maze_generation_position(10)
    print(f"test = {starting_maze_generation_position_h} - {starting_maze_generation_position_w}")
    maze[starting_maze_generation_position_h][starting_maze_generation_position_w] = path
    walls = []
    walls = get_starting_walls(walls,starting_maze_generation_position_h,starting_maze_generation_position_w)
    maze = set_starting_walls(maze,starting_maze_generation_position_h,starting_maze_generation_position_w)
    make_maze_walls(maze,walls,10,10)
    return maze


def get_starting_walls(walls, start_h, start_w):
    '''
    This will add the walls surrounding the starting path to the walls list
    '''
    walls.append([start_h-1, start_w])
    walls.append([start_h, start_w-1])
    walls.append([start_h, start_w+1])
    walls.append([start_h+1, start_w])
    return walls


def set_starting_walls(maze, start_h, start_w):
    '''
    This will set the display of the maze to show the walls
    '''
    maze[start_h-1][start_w] = wall
    maze[start_h][start_w-1] = wall
    maze[start_h][start_w+1] = wall
    maze[start_h+1][start_w] = wall
    return maze


def starting_maze_generation_position(max_number):
    '''
    Get the starting posiiton for maze creation but stays away from the edge of the maze"
    '''
    starting_pos = int(random.random() * max_number)
    if starting_pos == 0:
        starting_pos += 1
    if starting_pos == max_number-1:
        starting_pos -= 1
    return starting_pos


def create_blank_maze():
    """
    creates a 2d array which stores the width and height of the maze
    """
    width = 10
    height = 10
    maze = []
    for h in range(0,height):
        row = []
        for w in range(0,width):
            row.append(open)
        maze.append(row)
    return maze


def draw_maze(maze):
    '''
    Draw the grid to the console
    '''
    for h in range(0,10):
        for w in range(0,10):
            print(f"{maze[h][w]} ",end="")
        print()


def make_maze_walls(maze,walls,height,width):
    '''
    Prims Algorithm 
    While there are walls in the list:
    Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
    Make the wall a passage and mark the unvisited cell as part of the maze
    Add the neighboring walls of the cell to the wall list.
    Remove the wall from the list
    '''
    surrounding_cell_count = 0
    while walls:
        # Pick a random wall
        rand_wall = walls[int(random.random()*len(walls))-1]

        # Check if it is a left wall
        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1]-1] == open and maze[rand_wall[0]][rand_wall[1]+1] == path:

                surrounding_cell_count = surroundingCells(maze,rand_wall)
                if surrounding_cell_count < 2:

                    maze[rand_wall[0]][rand_wall[1]] = path

                    # Make the walls
                    # The top wall
                    if rand_wall[0] != 0:
                        if maze[rand_wall[0]-1][rand_wall[1]] != path:
                            maze[rand_wall[0]-1][rand_wall[1]] = wall
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Bottom wall
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != path):
                            maze[rand_wall[0]+1][rand_wall[1]] = wall
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    # left wall
                    if (rand_wall[1] != 0):	
                        if (maze[rand_wall[0]][rand_wall[1]-1] != path):
                            maze[rand_wall[0]][rand_wall[1]-1] = wall
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                # Delete wall
                for single_wall in walls:
                    if (single_wall[0] == rand_wall[0] and single_wall[1] == rand_wall[1]):
                        walls.remove(single_wall)
                continue

        # Check if it is a top wall
        if rand_wall[0] != 0:
            if maze[rand_wall[0]-1][rand_wall[1]] == open and maze[rand_wall[0]+1][rand_wall[1]] == path:

                surrounding_cell_count = surroundingCells(maze,rand_wall)
                if surrounding_cell_count < 2:

                    maze[rand_wall[0]][rand_wall[1]] = path

                    # Make the walls
                    # top wall
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != path):
                            maze[rand_wall[0]-1][rand_wall[1]] = wall
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

				    # left wall
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != path):
                            maze[rand_wall[0]][rand_wall[1]-1] = wall
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

				    # right wall
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != path):
                            maze[rand_wall[0]][rand_wall[1]+1] = wall
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for single_wall in walls:
                    if (single_wall[0] == rand_wall[0] and single_wall[1] == rand_wall[1]):
                        walls.remove(single_wall)
                continue

        # Check if it is a bottom wall
        if rand_wall[0] != height -1:
            if maze[rand_wall[0]+1][rand_wall[1]] == open and maze[rand_wall[0]-1][rand_wall[1]] == path:

                surrounding_cell_count = surroundingCells(maze,rand_wall)
                if surrounding_cell_count < 2:

                    maze[rand_wall[0]][rand_wall[1]] = path

                    # Make the walls
                    # bottom wall
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != path):
                            maze[rand_wall[0]+1][rand_wall[1]] = wall
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    # left wall
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != path):
                            maze[rand_wall[0]][rand_wall[1]-1] = wall
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                    # right wall
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != path):
                            maze[rand_wall[0]][rand_wall[1]+1] = wall
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for single_wall in walls:
                    if (single_wall[0] == rand_wall[0] and single_wall[1] == rand_wall[1]):
                        walls.remove(single_wall)
                continue


        # Check if it is a right wall
        if rand_wall[1] != width-1:
            if maze[rand_wall[0]][rand_wall[1]+1] == open and maze[rand_wall[0]][rand_wall[1]-1] == path:

                surrounding_cell_count = surroundingCells(maze,rand_wall)
                if surrounding_cell_count < 2:

                    maze[rand_wall[0]][rand_wall[1]] = path

                    # Make the walls
                    # right wall
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != path):
                            maze[rand_wall[0]][rand_wall[1]+1] = wall
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                    # bottom wall
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != path):
                            maze[rand_wall[0]+1][rand_wall[1]] = wall
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    # top wall
                    if rand_wall[0] != 0:	
                        if maze[rand_wall[0]-1][rand_wall[1]] != path:
                            maze[rand_wall[0]-1][rand_wall[1]] = wall
                        if [rand_wall[0]-1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0]-1, rand_wall[1]])

        # Delete wall
        for single_wall in walls:
            if (single_wall[0] == rand_wall[0] and single_wall[1] == rand_wall[1]):
                walls.remove(single_wall)
        continue


def surroundingCells(maze,rand_wall):
    '''
    get all paths surrounding the wall
    '''
    s_cells = 0
    if maze[rand_wall[0]-1][rand_wall[1]] == path:
        s_cells += 1
    if maze[rand_wall[0]+1][rand_wall[1]] == path:
        s_cells += 1
    if maze[rand_wall[0]][rand_wall[1]-1] == path:
        s_cells +=1
    if maze[rand_wall[0]][rand_wall[1]+1] == path:
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
test_maze=create_maze()
draw_maze(test_maze)