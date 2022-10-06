# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint
import random

path = 'p'
wall = 'w'


def create_maze():
    maze = create_blank_maze()
    starting_maze_generation_position_h = starting_maze_generation_position(10)
    starting_maze_generation_position_w = starting_maze_generation_position(10)
    print(f"test = {starting_maze_generation_position_h} - {starting_maze_generation_position_w}")
    return maze


def starting_maze_generation_position(max_number):
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
            row.append(path)
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