#!/usr/bin/env python3
import argparse
from io import TextIOWrapper
import os
from simple_term_menu import TerminalMenu
from shutil import which

FILENAME: str = os.path.dirname(os.path.abspath(__file__)) + "/commands.txt"
parser = argparse.ArgumentParser(description='Save your commands and reuse them')

def print_help():
    parser.print_help()

def is_tool(name: str):
    return which(name.split(' ')[0]) is not None

def get_commands_array(file: TextIOWrapper) -> list[str]:
    commands = file.read().splitlines()
    return commands

def save_commands_to_file(commands: list[str], file: TextIOWrapper):
    file.seek(0)
    for command in commands:
        file.write(command + '\n')

def display_commands_choice():
    file = open(FILENAME, "r")
    commands = get_commands_array(file);
    if not commands:
        print("There are no commands saved yet")
        print_help()
        return
    terminal_menu = TerminalMenu(commands, search_key=None, show_search_hint=True, show_search_hint_text="Type any character rzawto search a command")
    menu_entry_index = terminal_menu.show()
    if menu_entry_index is None:
        return
    selected_command=commands[menu_entry_index]
    if is_tool(selected_command):
        os.system(selected_command)
    else:
        print(selected_command, "is not a command")
    file.close()

def add_command():
    file = open(FILENAME, "r+")
    commands = get_commands_array(file)
    command_to_add=input("Enter the new command:\n")
    if not is_tool(command_to_add):
        print(command_to_add, "is not a command")
        return
    elif command_to_add in commands:
        print(command_to_add, "is already saved")
        return
    if command_to_add:
        commands.append(command_to_add)
        save_commands_to_file(commands=commands, file=file)
        print("The command", "\'" + command_to_add + "\'", "was succesfully saved")
    file.close()

def remove_command():
    file = open(FILENAME, "r+")
    commands = get_commands_array(file)
    terminal_menu = TerminalMenu(commands)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index is None:
        print("You did not select a command to remove")
        return
    command_to_remove=commands[menu_entry_index]
    if command_to_remove not in commands:
        print("This command cannot be removed: it is not saved")
    if command_to_remove:
        commands.remove(command_to_remove)
        save_commands_to_file(commands=commands, file=file)
        print("The command","\'" + command_to_remove + "\'", "was succesfully removed")
    file.close()

def main():

    parser.add_argument('-a', '--add', action="store_true", help='add a command')
    parser.add_argument('-r', '--remove', action="store_true", help='remove a command')

    arguments = parser.parse_args()

    if arguments.add:
        add_command()
    elif arguments.remove:
        remove_command()
    else:
        display_commands_choice()

if __name__ == '__main__':
    main()
    