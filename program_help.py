"""
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

"""
from util import (warning_text_color, clear_terminal, highlight_text_color,
                  press_enter, heading_text_color, positive_text_color)


def help_popup(menu_call):
    """
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
    """
    clear_terminal()
    show_help_heading()

    if menu_call == 1:
        main_menu_help()
    elif menu_call == 2:
        maze_menu_help()
    elif menu_call == 3:
        graph_menu_help()
    show_help_footer()
    if menu_call != 3:
        press_enter()


def show_help_heading():
    """
    Will show the heading for the help
    """
    print(f"{highlight_text_color('===========================')}"
          f"{warning_text_color(' Help Information ')}"
          f"{highlight_text_color('===========================')}")


def show_help_footer():
    """
    Will show the footing for the help
    """
    print(f"{highlight_text_color('=====================================')}"
          f"{highlight_text_color('===================================')}")


def main_menu_help():
    """
    help information for the main menu
    """
    print(heading_text_color("\033[4mOption 1 - Create Maze\033[0m"))
    print("A maze is a path or collection of paths, typically from an\n"
          "entrance to a goal. This option will ask you to enter a name for\n"
          "your maze. Then enter the width and height. Once the data is in,\n"
          "it will create a random designed maze")
    print()
    print(heading_text_color("\033[4mOption 2 - Create Graph\033[0m"))
    print("This will enable you to create a graph and add your own\n"
          "connections. It will also allow you to run various algorithms\n"
          "to the graph.")
    print()
    print("A Graph is a non-linear data structure consisting of vertices &\n"
          "edges. The vertices and edges are sometimes also referred to as\n"
          "nodes and links. links are lines or arcs that connect any two\n"
          "nodes in the graph. Each link/edge will have a weight, they can\n"
          "also have a direction. This could be the distance, cost, time\n"
          "taken to get from one node to another. Below is an example.")
    print()
    print("The london tube map can have the stations as nodes and the lines\n"
          "tracks as links/edges. You can then work out the quickest route\n"
          "from one stop to another. An example of this is stored in Google\n"
          "sheets. Load in 'tube_map' to use the zone 1 & 2 London tube map\n"
          "example.")
    print()
    print(positive_text_color("Press enter to see page 2"))
    print()
    press_enter()
    clear_terminal()
    show_help_heading()
    print()
    print(positive_text_color("Page 2"))
    print()
    print(heading_text_color("\033[4mOption 3 - Load Maze from file\033[0m"))
    print("This will show you all the mazes that have been previously saved.\n"
          "You can type in the name of the maze you want to load in and use\n"
          "in the program.")
    print()
    print(heading_text_color("\033[4mOption 4 - Load Graph from file\033[0m"))
    print("This will show you the graphs that have been previously saved.\n"
          "You can type in the name of the graph you want to load in and use\n"
          "in the program.")
    print()
    print(heading_text_color("\033[4mOption 5 - Delete Maze\033[0m"))
    print("This will show you the mazes that have been previously saved.\n"
          "You can type in the name of the maze you want to delete.")
    print()
    print(heading_text_color("\033[4mOption 6 - Delete Graph\033[0m"))
    print("This will show you the graphs that have been previously saved.\n"
          "You can type in the name of the graph you want to delete.")
    print()


def maze_menu_help():
    """
    help information for the maze menu
    """
    print(heading_text_color("\033[4mOption 1 - Solve /Unsolve Maze\033[0m"))
    print("This will show the solution to the maze or remove the solution\n"
          "from the maze")
    print()
    print(heading_text_color("\033[4mOption 2 - Save maze to file\033[0m"))
    print("This will save te current state of your maze so you can load it\n"
          "in at another time")
    print()
    print(heading_text_color("\033[4mOption 3 - User Solve Maze\033[0m"))
    print("This will allow you to solve the maze by moving a blue square\n"
          "from the start of the maze to the end.\n")
    print("Controls to move: (W - Up, S - Down, D - Right, A - Left) then\n"
          "press Enter")
    print()


def graph_menu_help():
    """
    help information for the graph menu
    """
    print(heading_text_color("\033[4mOption 1 - Add Node\033[0m"))
    print("This will add a node to the graph. A graph node is also known\n"
          "as graph vertex. It is a point on which the graph is defined\n"
          "and maybe connected by graph edges.")
    print()
    print(heading_text_color("\033[4mOption 2 - Add Link\033[0m"))
    print("This will add a link between two nodes in the graph. An edge\n"
          "(or link) of a graph is one of the connections between the\n"
          "nodes of the graph.")
    print()
    print(heading_text_color("\033[4mOption 3 - Delete Link\033[0m"))
    print("This will remove a link between two nodes. You will need to know\n"
          "the names of the two nodes you are removing the link of.")
    print()
    print(heading_text_color("\033[4mOption 4 - Delete Node\033[0m"))
    print("This will remove a node from the graph. You will need to know\n"
          "the name of the node you are removing")
    print()
    print(heading_text_color("\033[4mOption 5 - Save Graph\033[0m"))
    print("This will save the current state of your graph so you can load\n"
          "it in at another time")
    print()
    print(positive_text_color("Press enter to see page 2"))
    press_enter()
    clear_terminal()
    show_help_heading()
    print()
    print(positive_text_color("Page 2"))
    print()
    print(heading_text_color("\033[4mOption 6 - Show Graph Details\033[0m"))
    print("This will show all the details for the graph and will ask you if\n"
          "you want to view the complete matrix. You can press '0' to go\n"
          "back to the menu or '1' to view the full matrix.")
    print()
    print(heading_text_color("\033[4mOption 7 - Fill With Sample Data\033[0m"))
    print("This will add sample data to the graph.")
    print()
    print(heading_text_color("\033[4mOption 8 - Show Connections\033[0m"))
    print("This will ask you to enter the name of the node you want to view.\n"
          " It will then show all the weights & connections for that node.\n")
    print()
    print(heading_text_color("\033[4mOption 9 - Find Shortest Route\033[0m"))
    print("This will find the shortest path to get from one node to another\n"
          "node in the graph. It will tell you the steps to take inorder to\n"
          "get there.")
    print()
    print(heading_text_color("\033[4mOption 10 - Minimum Spanning Tree"
                             "\033[0m"))
    print("This will create a minimum spanning tree. A spanning tree means\n"
          "all nodes must be connected and they must be connected with the\n"
          "minimum weight link to make it a Minimum Spanning Tree.")
    print()
