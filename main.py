from collections import OrderedDict
import json
import sys
import os


def runCommandLineMenu(list_of_programs_passed):
    print("Welcome to Python Code Vault!")
    print("Choose a type of program to run:")
    print("1 => Selection of curated exercises.")
    print("2 => Demonstration of sort types.")
    user_input_selection = int(input("\n(Enter the number corresponding with the program) => "))
    printMenuOfSelections(list_of_programs_passed[user_input_selection-1])


def printMenuOfSelections(list_of_files):
    x = 0
    print("The list of files is a " + str(type(list_of_files)))
    print(list_of_files.get("title"))
    for obj in list_of_files:
        print(obj + str(type(obj)))

    user_input_selection = int(input("\n(Enter the number corresponding with the program) => "))
    os.system("sudo python ./" + list_of_files.get(user_input_selection)[1])


if __name__ == '__main__':
    with open('./list_of_programs.json') as file:
        list_of_programs = json.load(file)

    if len(sys.argv) < 2:
        runCommandLineMenu(list_of_programs)

