# coding=utf-8
""" Wonder who reads these... I mean, besides me """

import random;

"""

Help Menu print out

"""


def print_help_menu():
    print("Instructions of this program:\n");
    print("Avoid writing \"[\" or \"]\", these are used to determine where a certain variable or command is expected.")
    print("[main]:   The main list is the one that gets randomized and edited");
    print("[deri]:   The deri(vative) list gets generated using the 'gen' command.\n");
    print("rand [a] [b]    Randomize the set of numbers of the main list, from [a] to [b]");
    print("set  [n]        Set [n] amount of numbers to be the size of the main list.\n");
    print("gen -l [n]      Generate a derivative list from main, with items lesser than [n].");
    print("gen -e [n]      Generate a derivative list from main, with items equal to [n].");
    print("geb -g [n]      Generate a derivative list from main, with items greater than [n].\n");
    print("sort [list] lg  Sort (main/deri) from lesser to greatest number");
    print("sort [list] gl  Sort (main/deri) from the greatest to lesser number\n");
    print("print [list]    Prints the (main/deri) list.\n");
    print("help            You get to see me once more.");
    print("exit            Exits the program.\n");


def print_secret_scroll():
    print("easter bugs make me strong... meow");
    print("- -- .-.");
    print("- - /  |                - - /|_/|      .-------------------.");
    print("   /   |  - _______________| @.@|     /    Bruno Köppel     )");
    print("- |    |-- (______         >\\_C/< ---/                     /");
    print("  |    |  -  -   / ______  _/____)  (   Brunokoppel.com   /");
    print("-- \\   | -  -   / /\\ \\   \\ \\         `-------------------'");
    print(" -  \\  |     - (_/  \\_) - \\_)");
    print("- -  | |\n\n");


""" Functionality methods """


def process_user_command_line_input(prompt):
    user_input_command = str(input(prompt));
    command_result = [];

    if VERBOSE1:
        print(user_input_command);

    while len(user_input_command) > 0:
        if VERBOSE1:
            print(len(user_input_command));

        space_index = user_input_command.find(" ");

        if VERBOSE1:
            print(space_index);

        if space_index == -1:
            space_index = len(user_input_command);
        else:
            """ [:end] gets all characters from the beginning of the string to the variable end. """
            command_result.append(user_input_command[:space_index]);
            user_input_command = user_input_command[space_index:];

        if VERBOSE1:
            print(space_index);
            print(command_result);
            print(user_input_command);

    return command_result;


def ask_user_number_input(prompt):
    user_input = input(prompt);
    while not user_input.isdigit():
        user_input = input("Not an integer, try again: ");
    return int(user_input);


def check_user_input_command(prompt):
    user_input = input(prompt);
    if user_input.isdigit:
        return user_input;
    else:
        return None;


def check_number_input_command(number):
    if number.isdigit:
        return int(number);
    else:
        print("\nString was given, instead of a number\n");
        return None;


""" 

Program Methods

"""


def generate_random_numbers_for_list(min_range, max_range):
    return random.randrange(minimumRange, maximumRange);


def generate_list(min_range, max_range, main_list, number_in_list):
    for x in range(0, number_in_list):
        new_number = random.randrange(min_range, max_range);
        mainList.append(new_number);


def generate_derived_list(condition, number):
    temporal_list = [];

    if condition == "-l":
        for x in mainList:
            if x < number:
                temporal_list.append(x);

    elif condition == "-e":
        for x in mainList:
            if x == number:
                temporal_list.append(x);

    elif condition == "-g":
        for x in mainList:
            if x > number:
                temporal_list.append(x);

    elif condition is None:
        print("You didn't enter a condition, check 'help' if you aren't sure.");

    else:
        print("Invalid command entered, check 'help' if you aren't sure.")

    return temporal_list;


def sort_list(list_given, condition):
    if condition == "lg":
        for xIndex in list_given:
            for yIndex in list_given:
                if yIndex < xIndex:
                    list_given[xIndex], list_given[yIndex] = list_given[yIndex], list_given[xIndex]

    elif condition == "gl":
        for xIndex in list_given:
            for yIndex in list_given:
                if yIndex > xIndex:
                    list_given[xIndex], list_given[yIndex] = list_given[yIndex], list_given[xIndex]

    elif condition is None:
        print("Condition not given");

    else:
        print("Condition not recognized");

    return list_given;


""" 

WELCOME TEXT

BEGINNING OF THE APPLICATION

"""

print("Welcome to the 3rd Exercise: ");
print_help_menu();

VERBOSE1 = False;
VERBOSE2 = True;

""" 

Variables for the list, and variables related to it 

"""

mainList = [];
mainListAmountOfNumber = 0;
derivedList = [];

minimumRange = 0;
maximumRange = 1;

machineState = True;
while machineState:
    random.seed();

    command = process_user_command_line_input("Exercise3@YourChoice~$ ");
    print("Command entered:\n");
    print(command);

    if command[0] == "exit":
        print("Bye bye.. :)");
        machineState = False;

    elif command[0] == "help":
        print_help_menu();

    elif command[0] == "rand":
        if command[1] is None:
            minimumRange = ask_user_number_input("Specify minimum range for random number generation: ")
        else:
            minimumRange = command[1];

        if command[2] is None:
            minimum_range = ask_user_number_input("Specify maximum range for random number generation: ")
        else:
            maximum_range = command[2];

        if len(mainList) != 0:
            for index in mainList:
                mainList[index] = generate_random_numbers_for_list(minimum_range, maximum_range);
        else:
            print("\nThe range of values is updated, however your list is empty.\nRun 'set' commmand, to set a size "
                  "to it.\n\n");

    elif command[0] == "set":
        if check_number_input_command(command[1]) > 0:
            for index in range(0, int(command[1])):
                mainList.append(generate_random_numbers_for_list(minimum_range, maximum_range));

        elif command[1] is None:
            print("Value not given");

        else:
            print("Error, value is zero or below.");

    elif command[0] == "gen":
        derivedList = generate_derived_list(command[1], command[2]);

    elif command[0] == "sort":
        if command[1] == "main":
            mainList = sort_list(mainList, command[2]);

        elif command[1] == "deri":
            derivedList = sort_list(derivedList, command[2]);

        elif command[1] is None:
            print("List not given");

        else:
            print("List not recognized");

    elif command[0] == "print":
        if command[1] == "main":
            print(mainList);

        elif command[1] == "deri":
            print(derivedList);

        elif command[1] is None:
            print("List not given");

        else:
            print("List not recognized");

    elif command[0] == "bko":
        print_secret_scroll();

    else:
        print("Command not recognized");

"""

I'm gonna pretend like I forgot to delete this,
yours truly,
bko

"""
