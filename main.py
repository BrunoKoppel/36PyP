from collections import OrderedDict
import json
import sys
import os


def getUserInput():
    user_input_selection = input("\n(Enter the number corresponding with the program) => ")
    if user_input_selection.isdigit():
        return user_input_selection

    print("Command entered is not a valid selection, try again...")
    return 0


def runCommandLineMenu(list_of_programs_passed):
    print("Welcome to Python Code Vault!")
    print("Choose a type of program to run:")
    print("1 => Selection of curated exercises.")
    print("2 => Demonstration of sort types.")
    printMenuOfSelections(list_of_programs_passed[getUserInput()-1])


def printMenuOfSelections(list_of_files):
    x = False
    for obj in list_of_files:
        if x:
            print(list_of_files.get(obj))
            x = True
        else:
            print(obj + ". => " + list_of_files.get(obj)[0])

    user_input_selection = getUserInput()
    if user_input_selection != 0 and user_input_selection < len(list_of_files):
        os.system("python ./" + list_of_files.get(str(user_input_selection))[1])


if __name__ == '__main__':
    with open('./list_of_programs.json') as file:
        list_of_programs = json.load(file)

    if len(sys.argv) < 2:
        runCommandLineMenu(list_of_programs)
        print("End of Program reached")

