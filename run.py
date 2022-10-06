# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint


path = 'p'
wall = 'w'


def create_maze():
    width = 10
    height = 10
    maze = []
    for h in range(0,height):
        row = []
        for w in range(0,width):
            row.append(path)
        maze.append(row)
    pprint(maze)
    return maze




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
create_maze()