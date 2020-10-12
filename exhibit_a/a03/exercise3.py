# coding=utf-8
""" Wonder who reads these... I mean, besides me """

import random;

""" Help Menu print out"""

def printHelpMenu():
	print("Instructions of this program:\n");
	print("-rand [a] [b]	Randomize the set of numbers of the main list, from [a] to [b]");
	print("-set  [n]		Set [n] amount of numbers to be the size of the main list.\n");
	print("-cs [n]			create a derivarive list from main, with items smaller than [n].");
	print("-ce [n]			create a derivarive list from main, with items equal to [n].");
	print("-cb [n]			create a derivarive list from main, with items bigger than [n].\n");
	print("-so sg			Sort the list from smaller to greatest number");
	print("-so gs			Sort the list from the greatest to smaller number\n");
	print("-pr main			Prints the main list.");
	print("-pr deri			Prints the derivative list\n");
	print("-he				You get to see me once more.");
	print("-ex				Exits the program.\n");
    
def printSecretScroll():
	print("easter bugs make me strong... meow");
	print("- -- .-.");
	print("- - /  |                - - /|_/|      .-------------------.");
	print("   /   |  - _______________| @.@|     /    Bruno Köppel     )");
	print("- |    |-- (______         >\_C/< ---/                     /");
	print("  |    |  -  -   / ______  _/____)  (   Brunokoppel.com   /");
	print("-- \   | -  -   / /\ \   \ \         `-------------------'");
	print(" -  \  |     - (_/  \_) - \_)");
	print("- -  | |\n\n");



""" Functionality methods """

def processUserCommandLineInput(prompt):
	userInputCommand = str(input(prompt));
	spaceIndex = userInputCommand.find(" ");
	
	if (spaceIndex == -1):
		spaceIndex = len(userInputCommand);
	
	command = [userInputCommand[:spaceIndex], userInputCommand[spaceIndex+1:]];
	return command;

def checkUserInput(prompt):
    userInput = input(prompt);
    while (userInput.isdigit() == False):
        userInput = input("Sorry try again, " + prompt);
    print("Thank you!\n");
    return int(userInput);

def checkUserInputCommand(prompt):
    userInput = input(prompt);
    if (userInput.isdigit):
        return userInput;
    else:
        return None;


""" 

	Welcome text 

"""

print("Welcome to the 3rd Exercise: ");
printHelpMenu();



""" 

	Variables for the list, and variables related to it 
	
"""

mainList = [];
derivedList = []; 

maximumRange = 1;
minimumRange = 0;

machineState = True;
while (machineState):
	
	command = processUserCommandLineInput("Exercise3@YourChoice~$ ");
	
	if (command[0] == "-ex"):
		print("Bye bye.. :)");
		machineState = False;
	
	elif (command[0] == "-he"):
		printHelpMenu();
		
	elif (command[0] == "-rand"):
		random.seed();
		
		if (len(mainList) != 0)
			for x in mainList:
				x = random.randrange(command[1], command[2]);
				
		
		
	elif (command[0] == "-set"):
		
		
	elif (command[0] == "-cs"):
		
		
	elif (command[0] == "-ce"):
		
		
	elif (command[0] == "-cb"):
		
		
	elif (command[0] == "-so"):
		
		
	elif (command[0] == "-pr"):
		
		
	elif (command[0] == "bko"):
		printSecretScroll();
	
	else:
		print("Command not recognized");	
	

	print(a);

"""

	I'm gonna pretend like I forgot to delete this just for effects
	
"""
