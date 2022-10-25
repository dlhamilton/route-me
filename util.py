'''
utilites module for route me

Classes:

    None

Functions:

    positive_text_color(str) -> str
    warning_text_color(str) -> str
    negative_text_color(str) -> str
    highlight_text_color(str) -> str
    heading_text_color(str) -> str
    get_number_option(str, int, int) -> int
    valid_user_input(str) -> boolean

Variables:

    SCOPE
    CREDS
    SCOPED_CREDS
    GSPREAD_CLIENT
    SHEET

'''
import re
import gspread
from termcolor import colored
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('route_me_data')


def positive_text_color(text):
    '''
    green text style

    Parameters
    ----------
    text: str
        the output string

    Returns
    -------
    coloured text: str
        the string with a new colour
    '''
    return colored(text, 'green')


def warning_text_color(text):
    '''
    yellow text style

    Parameters
    ----------
    text: str
        the output string

    Returns
    -------
    coloured text: str
        the string with a new colour
    '''
    return colored(text, 'yellow')


def negative_text_color(text):
    '''
    red text style

    Parameters
    ----------
    text: str
        the output string

    Returns
    -------
    coloured text: str
        the string with a new colour
    '''
    return colored(text, 'red')


def highlight_text_color(text):
    '''
    cyan text style

    Parameters
    ----------
    text: str
        the output string

    Returns
    -------
    coloured text: str
        the string with a new colour
    '''
    return colored(text, 'cyan')


def heading_text_color(text):
    '''
    magenta text style

    Parameters
    ----------
    text: str
        the output string

    Returns
    -------
    coloured text: str
        the string with a new colour
    '''
    return colored(text, 'magenta')


def valid_user_input(text):
    '''
    validate the user input to make sure it starts with a letter

    Parameters
    ----------
    text: str
        the users input

    Returns
    -------
    if the text meets al requirements returns true
    '''
    if len(text) < 1:
        print(negative_text_color("Input is not long enough"))
        return False
    if re.search("^[a-zA-Z]", text) is None:
        print(negative_text_color("Input must start with a letter"))
        return False

    return True


def get_number_option(name, start, end):
    '''
    numerical menu
    get the user to enter a number and will validate their entry

    Parameters
    ----------
    name: str
        menu name
    start: int
        min number the user can select
    end: int
        max number the user can select

    Returns
    -------
    menu option: int
        the menu number the user has selected
    '''
    invalid_option = True
    while invalid_option:
        try:
            invalid_option = True
            menu_option = int(input(f"Please enter your {name} "
                                    f"choice ({start} - {end}):\n"))
        except ValueError:
            print(negative_text_color(f"Not a valid number - Please enter a "
                  f"number between {start} and {end}"))
        else:
            if menu_option >= start and menu_option <= end:
                invalid_option = False
            else:
                print(negative_text_color(f'Number option not avaliable '
                      f'- Please enter a number between {start} and {end}'))
    return menu_option
