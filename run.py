"""
route-me

This program is designed to help you find the quickest way from a
start position to a destination.
It can also create and solve mazes. When you start the program
you will be taken to the Main menu.

Classes:

    None

Functions:

    show_menu()
    show_maze_menu()
    show_graph_menu()
    menu_option_1(object = None)
    menu_option_2(object = None)
    show_app_title()
    get_saved_file_names(int, str)
    load_graph(str) -> object
    load_maze(str) -> object
    exit_message()
    main()

Variables:

    None

"""
from termcolor import colored
from colorama import init, Fore, Back
from game_graph import GameGraph
from game_maze import GameMaze
from util import (positive_text_color, warning_text_color, negative_text_color,
                  highlight_text_color, heading_text_color, valid_user_input,
                  get_number_option, SHEET, clear_terminal, press_enter)
from program_help import help_popup
# reset colour back to default
init(autoreset=True)


def show_menu():
    """
    show the main menu to the console
    """
    print(f"{colored('---------', 'cyan')} Menu "
          f"{colored('---------', 'cyan')} ")
    print(warning_text_color(
        "Enter the menu number you want then press enter."
    ))
    print("1) Create Maze")
    print("2) Create Graph")
    print("3) Load Maze from file")
    print("4) Load Graph from file")
    print("5) Delete Maze from file")
    print("6) Delete Graph from file")
    print("0) Exit")
    print(heading_text_color("Press 'H' for help and to get more details"))
    print(f"{colored('========================','cyan')}")


def show_maze_menu():
    """
    show the menu for the maze to the console
    """
    print()
    print(f"{colored('-------', 'cyan')} Maze Menu "
          f"{colored('-------', 'cyan')}")
    print(warning_text_color(
        "Enter the menu number you want then press enter."
    ))
    print("1) Solve/ Unsolve Maze")
    print("2) Save maze to file")
    print("3) User Solve Maze")
    print("0) Back to Main menu")
    print(heading_text_color("Press 'H' for help and to get more details"))
    print(f"{colored('=========================','cyan')}")


def show_graph_menu():
    """
    show the menu for the graph to the console
    """
    print(f"{colored('--------', 'cyan')} Graph Menu "
          f"{colored('--------', 'cyan')}")
    print(warning_text_color(
        "Enter the menu number you want then press enter."
    ))
    print("1) Add Node")
    print("2) Add Link")
    print("3) Delete Link")
    print("4) Delete Node")
    print("5) Save Graph")
    print("6) Show Graph Details")
    print("7) Fill With Sample Data")
    print("8) Show Connections for Node")
    print("9) Find Shortest Route")
    print("10) Minimum Spanning Tree")
    print("0) Back to Main menu")
    print(heading_text_color("Press 'H' for help and to get more details"))
    print(f"{colored('============================','cyan')}")


def menu_option_1(the_maze=None):
    """
    get the user input and perform the method the user selects for the maze

    Parameters
    ----------
    the_maze: maze
        if a maze has not been loaded, set maze to None

    Returns
    -------
    None
    """
    maze_name = "Untitled Maze"
    if the_maze is None:
        name_valid = False
        while name_valid is False:
            maze_name = input("Please enter the name of the maze:\n")
            name_valid = valid_user_input(maze_name)
        maze_size = get_number_option("maze size", 10, 40)
        the_maze = GameMaze(maze_size, maze_name)
    print(positive_text_color("Maze ready!"))
    press_enter()
    clear_terminal()
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
        elif maze_menu_option == 900:
            help_popup(2)
        clear_terminal()
        the_maze.draw_maze()
        show_maze_menu()
        maze_menu_option = get_number_option("maze menu", 0, 3)


def menu_option_2(the_graph=None):
    """
    get the user input and perform the method the user selects for the graph

    Parameters
    ----------
    the_graph: graph
        if a graph has not been loaded, set graph to None

    Returns
    -------
    None
    """
    graph_name = "Untitled Graph"
    if the_graph is None:
        name_valid = False
        while name_valid is False:
            graph_name = input("Please enter the name of the graph:\n")
            name_valid = valid_user_input(graph_name)
        the_graph = GameGraph(graph_name)
    print(positive_text_color("Graph ready!"))
    press_enter()
    clear_terminal()
    show_graph_menu()
    graph_menu_option = get_number_option("graph menu", 0, 10)
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
            clear_terminal()
            the_graph.show_graph_status()
        elif graph_menu_option == 7:
            the_graph.quick_fill_graph()
        elif graph_menu_option == 8:
            the_graph.show_connections()
        elif graph_menu_option == 9:
            the_graph.dijkstra_path()
        elif graph_menu_option == 10:
            the_graph.min_spanning_tree()
        elif graph_menu_option == 900:
            help_popup(3)
        press_enter()
        clear_terminal()
        show_graph_menu()
        graph_menu_option = get_number_option("graph menu", 0, 10)


def show_app_title():
    """
    show the Title logo for the route me app
    """
    print(Fore.GREEN + Back.WHITE + "=================")
    print(Fore.BLUE + Back.WHITE + "+-+-+-+-+-+-+-+-+")
    print(Fore.RED + Back.WHITE + "|R|o|u|t|e|-|M|e|")
    print(Fore.BLUE + Back.WHITE + "+-+-+-+-+-+-+-+-+")
    print(Fore.GREEN + Back.WHITE + "=================")
    print()


def get_saved_file_names(save_type, file_op):
    """
    show the user all the graphs and mazes that are saved and will
    allow the user to enter the worksheets name to load it or delete
    it

    Parameters
    ----------
    save_type: int
        1 - is to load a maze
        2 - is to load a graph

    file_op: str
        delete - delete from Google sheets
        load - load from Google sheets
    Returns
    -------
    None
    """
    print(warning_text_color("loading available files..."))
    saved_sheets = SHEET.worksheet('saves')
    saved_names = saved_sheets.col_values(save_type)
    clear_terminal()
    if len(saved_names) != 0:
        print(heading_text_color(f"{file_op.capitalize()} File"))
        print(warning_text_color(
            f"Type the name of the file you want "
            f"to {file_op}, then click enter.."))
        print(warning_text_color("Press '0' to go back"))
        print()
        print(f"Files available to {file_op}:")
        print(highlight_text_color("========================"))
        for name in saved_names:
            print(name)
        print(highlight_text_color("========================"))
        print()
        file_name_enetered = input(f"Please enter the file name you want " +
                                   f"to {file_op} (case sensitive) \n")
        if file_name_enetered in saved_names:
            if file_op == "delete":
                delete_file(saved_names, file_name_enetered, save_type)
                press_enter()
            elif save_type == 1:
                print(warning_text_color("Maze loading..."))
                loaded_maze = load_maze(file_name_enetered)
                print(positive_text_color("Maze loaded!"))
                menu_option_1(loaded_maze)
            elif save_type == 2:
                print(warning_text_color("Graph loading..."))
                loaded_graph = load_graph(file_name_enetered)
                print(positive_text_color("Graph loaded!"))
                menu_option_2(loaded_graph)
        else:
            if file_name_enetered != '0':
                print(negative_text_color("This sheet could not be found!"))
                press_enter()
    else:
        print(negative_text_color("No saved sheets"))
        press_enter()


def load_graph(sheet_name):
    """
    loads the data from the sheet and will create a new instance of graph
    with the data

    Parameters
    ----------
    sheet_name: str
        the name of the sheet to load

    Returns
    -------
    the_graph: graph object
        the graph that has been loaded from Google sheets
    """
    temp_graph = SHEET.worksheet(sheet_name)
    temp_graph_name = sheet_name
    temp_graph_node_names = temp_graph.row_values(1)
    temp_graph_node = temp_graph.get_all_values()
    temp_graph_node.pop(0)
    int_temp_graph_node = []

    for row in temp_graph_node:
        int_row = [int(num) for num in row]
        int_temp_graph_node.append(int_row)

    the_graph = GameGraph(temp_graph_name)
    the_graph.load_in_graph(temp_graph_name, temp_graph_node_names,
                            int_temp_graph_node)
    return the_graph


def load_maze(sheet_name):
    """
    loads the data from the sheet and will create a new instance of maze
    with the data

    Parameters
    ----------
    sheet_name: str
        the name of the sheet to load

    Returns
    -------
    the_maze: maze object
        the maze that has been loaded from Google sheets
    """
    temp_maze = SHEET.worksheet(sheet_name).get_all_values()
    temp_maze_name = sheet_name
    temp_maze_size = int(len(temp_maze[0]))
    current = None

    the_maze = GameMaze(temp_maze_size, temp_maze_name)
    if len(temp_maze) != len(temp_maze[0]):
        current = temp_maze.pop()
        current = [int(current[0]), int(current[1])]

    the_maze.load_in_maze(temp_maze_name, temp_maze, current)
    return the_maze


def delete_file(saved_names, file_name_enetered, save_type):
    """
    this removes the worksheet from the sheets file and will remove
    the worksheet name from the saves worksheet.

    Parameters
    ----------
    save_type: int
        1 - is to load a maze. The column in sheets
        2 - is to load a graph. The column in sheets

    saved_names: str[]
        the name of all the saved sheets

    file_name_enetered: str
        the file name that the user wants to delete

    Returns
    -------
    None
    """
    clear_terminal()
    print(heading_text_color("Delete File"))
    print(warning_text_color("Deleting please wait..."))

    saved_names.remove(file_name_enetered)

    removed_worksheet = SHEET.worksheet(file_name_enetered)
    SHEET.del_worksheet(removed_worksheet)

    saved_sheets = SHEET.worksheet('saves')
    if save_type == 1:
        col_letter = "A"
        saved_sheets.batch_clear(['A1:A'+str(1+len(saved_names))])
    else:
        col_letter = "B"
        saved_sheets.batch_clear(['B1:B'+str(1+len(saved_names))])

    for file_name in saved_names:
        saves_worksheet_len = len(saved_sheets.col_values(save_type))

        saved_sheets.update(col_letter + str(saves_worksheet_len+1), file_name)

    print(positive_text_color("Deleted!"))


def exit_message():
    """
    Message shown to the user when they end the program
    """
    clear_terminal()
    print()
    print(highlight_text_color("Thanks for using Route-Me"))
    print()
    show_app_title()
    print()


def main():
    """
    Main, the program start
    """
    menu_option = None
    while menu_option != 0:
        if menu_option == 1:
            menu_option_1(None)
        elif menu_option == 2:
            menu_option_2(None)
        elif menu_option == 3:
            get_saved_file_names(1, "load")
        elif menu_option == 4:
            get_saved_file_names(2, "load")
        elif menu_option == 5:
            get_saved_file_names(1, "delete")
        elif menu_option == 6:
            get_saved_file_names(2, "delete")
        elif menu_option == 900:
            help_popup(1)
        clear_terminal()
        show_app_title()
        print("Welcome to Route-me the best way to find the quickest route.\n")
        show_menu()
        menu_option = get_number_option("menu", 0, 6)
    exit_message()


main()
