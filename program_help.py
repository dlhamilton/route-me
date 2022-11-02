'''
help section module for route me

will show help guides to the user and explain how to use the program.

Classes:

    None

Functions:

    help_popup(int)
    show_help_heading()
    show_help_footer()
    main_menu_help()
    maze_menu_help()
    graph_menu_help()

Variables:

    None

'''
from util import (warning_text_color, clear_terminal, highlight_text_color,
                  press_enter, heading_text_color, positive_text_color)


def help_popup(menu_call):
    '''
    shows the help details to help the user navigate the current menu they are
    on.

    Parameters
    ----------
    menu_call: int
        the menu number to identify which menu made the call.

        1 = main menu
        2 = maze menu
        3 = graph menu

    Returns
    -------
    None
    '''
    clear_terminal()
    show_help_heading()

    if menu_call == 1:
        main_menu_help()
    elif menu_call == 2:
        maze_menu_help()
    elif menu_call == 3:
        graph_menu_help()
    show_help_footer
    if menu_call != 3:
        press_enter()


def show_help_heading():
    '''
    Will show the heading for the help
    '''
    print(f"{highlight_text_color('===========================')}"
          f"{warning_text_color(' Help Information ')}"
          f"{highlight_text_color('===========================')}")


def show_help_footer():
    '''
    Will show the footing for the help
    '''
    print(f"{highlight_text_color('=====================================')}"
          f"{highlight_text_color('===================================')}")


def main_menu_help():
    '''
    help information for the main menu
    '''
    print(heading_text_color("\033[4m" + "Option 1 - Create Maze" + "\033[0m"))
    print("A maze is a path or collection of paths, typically from an " +
          "entrance to a goal. This option will ask you to enter a name for " +
          "your maze. Then enter the width and height. Once the data is in, " +
          "it will create a random designed maze")
    print()
    print(heading_text_color("\033[4m" + "Option 2 - Create Graph" +
          "\033[0m"))
    print("This will enable you to create a graph and add your own " +
          "connections. It will also allow you to run various algorithms " +
          "to the graph.")
    print()
    print("A Graph is a non-linear data structure consisting of vertices & " +
          "edges. The vertices and edges are sometimes also referred to as " +
          "nodes and links. links are lines or arcs that connect any two " +
          "nodes in the graph. Each link/edge will have a weight, they can " +
          "also have a direction. This could be the distance, cost, time " +
          "taken to get from one node to another. Below is an example.")
    print()
    print("The london tube map can have the stations as nodes and the " +
          "lines/ tracks as links/edges. You can then work out the quickest " +
          "route from one stop to another. An example of this is " +
          "stored in Google sheets. Load in 'tube_map' to use the zone 1 " +
          "and 2 London tube map example.")
    print()
    print(positive_text_color("Press enter to see page 2"))
    print()
    press_enter()
    clear_terminal()
    show_help_heading()
    print()
    print(positive_text_color("Page 2"))
    print()
    print(heading_text_color("\033[4m" + "Option 3 - Load Maze from file" +
          "\033[0m"))
    print("This will show you all the mazes that have been previously " +
          "saved. You can type in the name of the maze you want to load " +
          "in and use in the program.")
    print()
    print(heading_text_color("\033[4m" + "Option 4 - Load Graph from file" +
          "\033[0m"))
    print("This will show you all the graphs that have been previously " +
          "saved. You can type in the name of the graph you want to load " +
          "in and use in the program.")
    print()


def maze_menu_help():
    '''
    help information for the maze menu
    '''
    print(heading_text_color("\033[4m" + "Option 1 - Solve /Unsolve Maze" +
          "\033[0m"))
    print("This will show you the solution to the maze or remove the " +
          "solution from the maze")
    print()
    print(heading_text_color("\033[4m" + "Option 2 - Save maze to file" +
          "\033[0m"))
    print("This will save te current state of your maze so you can load " +
          "it in at another time")
    print()
    print(heading_text_color("\033[4m" + "Option 3 - User Solve Maze" +
          "\033[0m"))
    print("This will allow you to solve the maze by moving a blue square " +
          "from the start of the maze to the end.")
    print("Controls to move: (W - Up, S - Down, D - Right, A - Left) then " +
          "press Enter")
    print()


def graph_menu_help():
    '''
    help information for the graph menu
    '''
    print(heading_text_color("\033[4m" + "Option 1 - Add Node" +
          "\033[0m"))
    print("This will add a node to the graph. A graph node is " +
          "also known as graph vertex. It is a point on which the " +
          "graph is defined and maybe connected by graph edges.")
    print()
    print(heading_text_color("\033[4m" + "Option 2 - Add Link" +
          "\033[0m"))
    print("This will add a link between two nodes in the graph. " +
          "An edge (or link) of a graph is one of the connections between " +
          "the nodes of the graph.")
    print()
    print(heading_text_color("\033[4m" + "Option 3 - Delete Link" +
          "\033[0m"))
    print("This will remove a link between two nodes. You will need to " +
          "know the names of the two nodes you are removing the link of.")
    print()
    print(heading_text_color("\033[4m" + "Option 4 - Delete Node" +
          "\033[0m"))
    print("This will remove a node from the graph. You will need to " +
          "know the name of the node you are removing")
    print()
    print(heading_text_color("\033[4m" + "Option 5 - Save Graph" +
          "\033[0m"))
    print("This will save the current state of your graph so you can load " +
          "it in at another time")
    print()
    print(positive_text_color("Press enter to see page 2"))
    press_enter()
    clear_terminal()
    show_help_heading()
    print()
    print(positive_text_color("Page 2"))
    print()
    print(heading_text_color("\033[4m" + "Option 6 - Show Graph Details" +
          "\033[0m"))
    print("This will show all the details for the graph and will ask you" +
          "if you want to view the complete matrix. You can press '0' to go " +
          "back to the menu or '1' to view the full matrix.")
    print()
    print(heading_text_color("\033[4m" + "Option 7 - Fill With Sample Data" +
          "\033[0m"))
    print("This will add sample data to the graph.")
    print()
    print(heading_text_color("\033[4m" + "Option 8 - Show Connections" +
          "\033[0m"))
    print("This wlll ask you to enter the name of the node you want to view." +
          " It will then show all the weights and connections for that node.")
    print()
    print(heading_text_color("\033[4m" + "Option 9 - Find Shortest Route" +
          "\033[0m"))
    print("This will find the shortest path to get from one node to another " +
          "node in the graph. It will tell you the steps to take inorder to " +
          "get there.")
    print()
    print(heading_text_color("\033[4m" + "Option 10 - Minimum Spanning Tree" +
          "\033[0m"))
    print("This will create a minimum spanning tree. A spanning tree means " +
          "all nodes must be connected and they must be connected with the " +
          "minimum weight link to make it a Minimum Spanning Tree.")
    print()
    show_help_footer()
