"""
game graph module for route me

Classes:

    GameGraph

Functions:

    None

Variables:

    None

"""
# Library for INT_MAX
import sys
import gspread
from prettytable import PrettyTable
from util import (positive_text_color, warning_text_color, negative_text_color,
                  highlight_text_color, heading_text_color, valid_user_input,
                  get_number_option, SHEET, clear_terminal, press_enter)


class GameGraph:
    """
    Graph Class
    ...

    Attributes
    ----------
    graph_name : str
        name of the graph
    graph_nodes : int[]
        graph weights between node
    graph_node_names : str[]
        graph names for each node
    loaded: boolean
        has the maze been saved before

    Methods
    -------
    add_node_to_graph:
        add node to the graph array

    add_link_to_graph(mode):
        change the value in the node array

    __get_node_index(search_string):
        get the index of the node from the name

    show_graph_status:
        output all the values linked to the graph

    quick_fill_graph:
        put set values into the graph

    delete_node:
        delete a node from the graph array

    show_connections:
        show all the connections for one of the nodes

    dijkstra_path:
        find the shortest path to a node

    __print_short_path(total_distance, previous_node, start_index,
                         end_index, reachable):
        write out the instructions on how to follow the shortest path

    load_in_graph(name, node_names, matrix):
        update the graph with the data from Google sheets

    save_graph:
        store the maze details to Google sheets

    min_spanning_tree:
        will construct and print the minimum span using the graph array.

    __get_min_distance(distances, processed):
        find the minimum distance between all the nodes not processed

    __show_span(previous):
        will print out the spanning tree for the user

    __show_all_node_names():
        will print out the names of all the nodes

    __show_complete_link_message(link_weight, first_ind, second_ind)
        will print out the confirmation message when a link has been edited

    __output_connections(nni, ind):
        will print out the connections of a certain node

    __method_heading(text):
        print the heading design for the graph methods

    __node_name_instructions():
        print the instructions for when a user enters a node name

    """
    def __init__(self, name):
        """
        Constructs all the necessary attributes for the graph object.
        ...

        Parameters
        ----------
            name : str
                name of the maze
        """
        # instance attribute
        self.graph_name = name
        self.graph_nodes = []
        self.graph_node_names = []
        self.loaded = False

    def add_node_to_graph(self):
        """
        add node to the graph array and add a
        new array item to all items in the array

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        check_one = False
        while check_one is False:
            check_one = True
            clear_terminal()
            self.__method_heading("Adding a node")
            self.__node_name_instructions()
            name = input("Please enter the name of the node:\n")
            name_in_array = self.__get_node_index(name)

            if len(name) == 0:
                name_in_array = -4
            else:
                if name[0] == " ":
                    name_in_array = -4

            if name_in_array == -1:
                self.graph_node_names.append(name)
                temp_array = []
                for _ in self.graph_node_names:
                    temp_array.append(-1)
                self.graph_nodes.append(temp_array)
                for none in range(len(self.graph_nodes)-1):
                    self.graph_nodes[none].append(-1)
                print(positive_text_color("Node added!"))
            elif name_in_array == -2:
                check_one = False
                press_enter()
            elif name_in_array == -3:
                print(highlight_text_color("Back to menu"))
            elif name_in_array == -4:
                print(negative_text_color("Invalid name!"))
            else:
                print(negative_text_color(f"{name} is already in the graph!"))

    def add_link_to_graph(self, mode):
        """
        change the value in the node array to represent a new link
        between nodes

        Parameters
        ----------
        mode: str
            if it is adding or editing the link between the nodes

        Returns
        -------
        None
        """
        check_one = False
        check_two = False

        while check_one is False:
            check_one = True
            clear_terminal()
            self.__method_heading(f"{mode} the link between nodes")
            self.__node_name_instructions()
            first_name = input("Please enter the name of the first node:\n")
            first_ind = self.__get_node_index(first_name)
            if first_ind > -1:
                while check_two is False:
                    check_two = True
                    self.__node_name_instructions()
                    second_name = input("Please enter the name of "
                                        "the second node:\n")
                    second_ind = self.__get_node_index(second_name)
                    if second_ind > -1:
                        if first_ind != second_ind:
                            print(highlight_text_color(
                                f"{mode} link between "
                                f"{self.graph_node_names[first_ind]} "
                                f"to {self.graph_node_names[second_ind]}"))
                            if mode == "Delete":
                                link_weight = -1
                            else:
                                link_weight = get_number_option("node weight",
                                                                0, 100)
                            self.graph_nodes[first_ind][second_ind] = \
                                link_weight
                            self.graph_nodes[second_ind][first_ind] = \
                                link_weight
                            self.__show_complete_link_message(link_weight,
                                                              first_ind,
                                                              second_ind)
                        else:
                            print(negative_text_color("Error: Cannot change "
                                                      "link node to itself"))
                    elif second_ind == -2:
                        check_two = False
                        press_enter()
                        clear_terminal()
                        self.__method_heading(f"{mode} the "
                                              "link between nodes")
                        print(
                            f"First node is: "
                            f"{self.graph_node_names[first_ind]}")
                    elif second_ind == -3:
                        print(highlight_text_color("Back to menu"))
                    else:
                        print(negative_text_color("Error: Name not "
                                                  "found in graph"))
            elif first_ind == -2:
                check_one = False
                press_enter()
            elif first_ind == -3:
                print(highlight_text_color("Back to menu"))
            else:
                print(negative_text_color("Error: Name not found in graph"))

    def __get_node_index(self, search_string):
        """
        iterate through the array to see what the index is of the
        string that is passed to it. If the string is not in the array
        it will return -1, will return -2 if the user wants to do a
        name search, return -3 if the user enters 0 to go back.

        Parameters
        ----------
        search_string: str
            name of the node to search for

        Returns
        -------
        index of the node (-1 if not found)
        index of the node (-2 if showing all nodes)
        index of the node (-3 if exiting method)
        """
        if search_string == "0":
            return -3
        elif search_string != "123":
            for name in self.graph_node_names:
                if name.upper() == search_string.upper():
                    return self.graph_node_names.index(name)
            return -1
        else:
            self.__show_all_node_names()
            return -2

    def show_graph_status(self):
        """
        output all the values linked to the graph

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.__method_heading("Graph Details")
        print(highlight_text_color("Graph name: ") + self.graph_name)
        print()
        print(highlight_text_color("Node names:"))

        graph_table = PrettyTable(["No.", "Node Name", "Num. of connections"])

        count = 0
        for node in self.graph_node_names:
            links = list(filter(lambda number: number >= 0,
                         self.graph_nodes[count]))
            graph_table.add_row([count, node, len(links)])
            count += 1
        print(graph_table)
        print()
        print("Enter '0' to go back or '1' to see more node details")

        user_input = get_number_option("details", 0, 1)
        if user_input == 1:
            count = 0
            print(highlight_text_color("Node matrix:"))
            for node in self.graph_nodes:
                print(heading_text_color(str(count)) + " " + str(node))
                count = count + 1

    def quick_fill_graph(self):
        """
        put set values into the graph to allow the user to see an example
        graph

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.graph_node_names = ["Zero", "One", "Two", "Three", "Four", "Five",
                                 "six", "seven", "eight"]
        self.graph_nodes = [[-1, 4, 0, -1, -1, -1, -1, 8, -1],
                            [4, -1, 8, -1, -1, -1, -1, 11, -1],
                            [0, 8, -1, 7, -1, 4, -1, -1, 2],
                            [-1, -1, 7, -1, 9, 14, -1, -1, -1],
                            [-1, -1, -1, 9, -1, 10, -1, -1, -1],
                            [-1, -1, 4, 14, 10, -1, 2, -1, -1],
                            [-1, -1, -1, -1, -1, 2, -1, 1, 6],
                            [8, 11, -1, -1, -1, -1, 1, -1, 7],
                            [-1, -1, 2, -1, -1, -1, 6, 7, -1]
                            ]
        print(positive_text_color("Data added!"))

    def delete_node(self):
        """
        delete a node from the graph array

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        check_one = False
        while check_one is False:
            check_one = True
            clear_terminal()
            self.__method_heading("Delete node")
            self.__node_name_instructions()
            node_name = input("Please enter the name of the node:\n")
            node_name_index = self.__get_node_index(node_name)
            if node_name_index > -1:
                count = len(self.graph_nodes)
                for node_index in range(count):
                    del self.graph_nodes[node_index][node_name_index]
                del self.graph_node_names[node_name_index]
                del self.graph_nodes[node_name_index]
                print(positive_text_color("Node removed!"))
            elif node_name_index == -2:
                check_one = False
                press_enter()
            elif node_name_index == -3:
                print(highlight_text_color("Back to menu"))
            else:
                print(negative_text_color("Error: Name not found in graph"))

    def show_connections(self):
        """
        show all the connections for one of the nodes

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        check_one = False
        while check_one is False:
            check_one = True
            clear_terminal()
            self.__method_heading("Show connected nodes")
            self.__node_name_instructions()
            node_name = input("Please enter the name of the node:\n")
            node_name_index = self.__get_node_index(node_name)
            if node_name_index > -1:
                has_link = False
                for ind, node in enumerate(self.graph_nodes[node_name_index]):
                    if node != -1:
                        has_link = True
                        nni = node_name_index
                        self.__output_connections(nni, ind)
                if has_link is False:
                    print(warning_text_color(
                        f"{self.graph_node_names[node_name_index]} has no "
                        f"links to other nodes"))
            elif node_name_index == -2:
                check_one = False
                press_enter()
            elif node_name_index == -3:
                print(highlight_text_color("Back to menu"))
            else:
                print(negative_text_color("Error: Name not found in graph"))

    def dijkstra_path(self):
        """
        find the shortest path to a node

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        check_one = False
        check_two = False

        while check_one is False:
            check_one = True
            clear_terminal()
            self.__method_heading("Shortest route")
            self.__node_name_instructions()
            start_name = input("Please enter the name of the start node:\n")
            start_name_index = self.__get_node_index(start_name)
            if start_name_index > -1:
                while check_two is False:
                    check_two = True
                    self.__node_name_instructions()
                    end_name = input("Please enter the name of the "
                                     "destination node:\n")
                    end_name_index = self.__get_node_index(end_name)
                    if end_name_index > -1:
                        total_distance = [sys.maxsize] * \
                            len(self.graph_node_names)
                        previous_node = [None] * len(self.graph_node_names)
                        total_distance[start_name_index] = 0
                        visited = [False]*len(self.graph_node_names)

                        for _ in range(len(self.graph_node_names)):
                            min_number = sys.maxsize
                            min_index = None
                            for node in range(len(self.graph_node_names)):
                                if total_distance[node] < min_number and \
                                        visited[node] is False:
                                    min_number = total_distance[node]
                                    min_index = node
                            current_node = min_index

                            visited[current_node] = True

                            for node in range(len(self.graph_node_names)):
                                if self.graph_nodes[current_node][node] >= 0 \
                                     and visited[node] is False and \
                                        total_distance[node] > \
                                        total_distance[current_node] + \
                                        self.graph_nodes[current_node][node]:
                                    total_distance[node] = \
                                        total_distance[current_node] + \
                                        self.graph_nodes[current_node][node]
                                    previous_node[node] = current_node
                        self.__print_short_path(total_distance, previous_node,
                                                start_name_index,
                                                end_name_index,
                                                visited[end_name_index])
                    elif end_name_index == -2:
                        check_two = False
                        press_enter()
                        clear_terminal()
                        self.__method_heading("Shortest route")
                        print(
                            f"Start node is: "
                            f"{self.graph_node_names[start_name_index]}")
                    elif end_name_index == -3:
                        print(highlight_text_color("Back to menu"))
                    else:
                        print(negative_text_color("Error: Name not found "
                                                  "in graph"))
            elif start_name_index == -2:
                check_one = False
                press_enter()
            elif start_name_index == -3:
                print(highlight_text_color("Back to menu"))
            else:
                print(negative_text_color("Error: Name not found in graph"))

    def __print_short_path(self, total_distance, previous_node, start_index,
                           end_index, reachable):
        """
        write out the instructions on how to follow the shortest path

        Parameters
        ----------
        total_distance: int[]
            the total distance of the path
        previous_node: int[]
            index of the node that was last visited
        start_index: int
            index of the start node
        end_index: int
            index of the end node
        reachable: boolean
            true if the start and end have a path to link

        Returns
        -------
        None
        """
        clear_terminal()
        self.__method_heading("Shortest route")
        if reachable is True:
            print(f"{self.graph_node_names[start_index]} to "
                  f"{self.graph_node_names[end_index]} has "
                  f"weight of {total_distance[end_index]} "
                  )
            the_node = end_index
            print()
            print(highlight_text_color("The steps to destination"))
            solution = []
            solution_name = []
            while the_node != start_index:
                solution.insert(0, the_node)
                solution_name.insert(0, self.graph_node_names[the_node])
                the_node = previous_node[the_node]
            solution_name.insert(0, self.graph_node_names[start_index])
            print(solution_name)
            last = start_index
            print()
            for index, node in enumerate(solution):
                print(f"{index+1}) {self.graph_node_names[last]} to "
                      f"{self.graph_node_names[node]} ("
                      f"{'weight = '}"
                      f"{highlight_text_color(self.graph_nodes[last][node])})")
                last = node
        else:
            print(negative_text_color(
                f"There is no route between "
                f"{self.graph_node_names[start_index]} and "
                f"{self.graph_node_names[end_index]}"))
        print()

    def load_in_graph(self, name, node_names, matrix):
        """
        update the graph with the data that was loaded from Google sheets

        Parameters
        ----------
        name: str
            name of the graph
        node_names: str[]
            name of all the node's
        matrix: int[]
            the array links of nodes

        Returns
        -------
        None
        """
        self.graph_name = name
        self.graph_node_names = node_names
        self.graph_nodes = matrix
        self.loaded = True

    def save_graph(self):
        """
        store the maze details to Google sheets

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        valid = False
        while valid is False:
            valid = True
            if self.loaded is True:
                SHEET.del_worksheet(SHEET.worksheet(self.graph_name))
            print(warning_text_color('Saving graph...(Please wait)'))
            try:
                new_sheet = SHEET.add_worksheet(self.graph_name,
                                                len(self.graph_node_names) + 1,
                                                len(self.graph_node_names))
            except gspread.exceptions.APIError:
                print(negative_text_color(
                    f"Could not save because: "
                    f"A sheet with the name "
                    f"{self.graph_name}' already exists."))
                valid = False
                name_valid = False
                new_name = None
                while name_valid is False:
                    new_name = input("Please enter a new name for the" +
                                     " sheet \n")
                    name_valid = valid_user_input(new_name)
                self.graph_name = new_name
            else:
                new_sheet.append_row(self.graph_node_names)
                for row in self.graph_nodes:
                    new_sheet.append_row(row)
                if self.loaded is False:
                    saves_worksheet = SHEET.worksheet('saves')
                    saves_worksheet_len = len(saves_worksheet.col_values(2))

                    saves_worksheet.update('B'+str(saves_worksheet_len+1),
                                           self.graph_name)
                print(positive_text_color("Graph saved!"))
                self.loaded = True

    def min_spanning_tree(self):
        """
        will construct and print the minimum span using the graph array.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        distances = [sys.maxsize] * len(self.graph_node_names)
        previous = [None] * len(self.graph_node_names)
        processed = [False] * len(self.graph_node_names)
        min_distance = None

        distances[0] = 0
        previous[0] = -1

        for _ in range(len(self.graph_node_names)):
            min_distance = self.__get_min_distance(distances, processed)

            if min_distance is None:
                break

            processed[min_distance] = True

            for node_int in range(len(self.graph_node_names)):
                if self.graph_nodes[min_distance][node_int] >= 0 and \
                    processed[node_int] is False and \
                        distances[node_int] > \
                        self.graph_nodes[min_distance][node_int]:
                    distances[node_int] = \
                        self.graph_nodes[min_distance][node_int]
                    previous[node_int] = min_distance

        if min_distance is not None:
            self.__show_span(previous)
        else:
            clear_terminal()
            self.__method_heading("Minimum Spanning Tree")
            print(negative_text_color("Error"))
            print(warning_text_color("Not all nodes are connected"))
            print(warning_text_color("Cannot make spanning tree"))

    def __get_min_distance(self, distances, processed):
        """
        find the minimum distance between all the nodes that have not been
        processed

        Parameters
        ----------
        distances: int[]
            the minimum distance value from the nodes

        processed: boolean[]
            if it has been processed in the spanning tree already

        Returns
        -------
        min_index: int
            the index position of the current shortest distance
        """
        min_num = sys.maxsize
        min_index = None
        for node_int in range(len(self.graph_node_names)):
            if distances[node_int] < min_num and \
              processed[node_int] is False:
                min_num = distances[node_int]
                min_index = node_int
        return min_index

    def __show_span(self, previous):
        """
        will print out the spanning tree for the user

        Parameters
        ----------
        previous: int[]
            the node that is previous to the node in that position in the
            node_names array

        Returns
        -------
        None
        """
        clear_terminal()
        self.__method_heading("Minimum Spanning Tree")

        graph_table = PrettyTable([heading_text_color("From"),
                                  heading_text_color("To"),
                                  heading_text_color("Weight")])

        for node_index in range(1, len(self.graph_node_names)):
            node_from = self.graph_node_names[previous[node_index]]
            node_to = self.graph_node_names[node_index]
            node_weight = self.graph_nodes[node_index][previous[node_index]]

            graph_table.add_row([warning_text_color(node_from),
                                positive_text_color(node_to),
                                highlight_text_color(node_weight)])
        print(graph_table)

    def __show_all_node_names(self):
        """
        will print out the names of all the nodes

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        temp_arr = []
        display_table = PrettyTable()
        display_table.title = heading_text_color("All nodes in the graph")
        display_table.header = False
        for cout, node_name in enumerate(self.graph_node_names, 1):

            temp_arr.append(node_name)
            if cout % 3 == 0:
                display_table.add_row(temp_arr)
                temp_arr = []

        arr_size = len(temp_arr)
        if arr_size != 0:
            for _ in range(3-arr_size):
                temp_arr.append("")
            display_table.add_row(temp_arr)
        print(display_table)

    def __show_complete_link_message(self, link_weight, first_ind, second_ind):
        """
        will print out the confirmation message when a link has been edited

        Parameters
        ----------
        link_weight: int
            the new weight of the link to decide what message to output

        first_ind: int
            The index that the link starts at

        second_ind: int
            The index that the link ends at

        Returns
        -------
        None
        """
        if link_weight != -1:
            print(
                f"{positive_text_color('Link Change Complete - ')}"
                f"{self.graph_node_names[first_ind]} to "
                f"{self.graph_node_names[second_ind]} "
                f"weight {link_weight}")
        else:
            print(
                f"{positive_text_color('Link Change Complete - ')}"
                f"{self.graph_node_names[first_ind]} to "
                f"{self.graph_node_names[second_ind]} "
                f"removed!")

    def __output_connections(self, nni, ind):
        """
        will print out the connections of a certain node

        Parameters
        ----------
        nni: int
            node name index, the index of the node being iterated

        ind: int
            index of the node that is connected to nni

        Returns
        -------
        None
        """
        print(
            f"{warning_text_color(self.graph_node_names[nni])} to "
            f"{positive_text_color(self.graph_node_names[ind])} "
            f"-- weight: "
            f"{highlight_text_color(self.graph_nodes[nni][ind])}")

    def __method_heading(self, text):
        """
        print the heading design for the graph methods

        Parameters
        ----------
        text: str
            the heading text

        Returns
        -------
        None
        """
        uline = ""
        for _ in range(len(text)):
            uline += "="
        print(heading_text_color(text))
        print(highlight_text_color(uline))

    def __node_name_instructions(self):
        """
        print the instructions for when a user enters a node name

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        print(
            positive_text_color("Type 0 "),
            " - ",
            warning_text_color("to go back to menu"))
        print(
            positive_text_color("Type 123 "),
            " - ",
            warning_text_color("to see all node names"))
