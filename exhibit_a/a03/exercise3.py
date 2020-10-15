# coding=utf-8
""" Wonder who reads these... I mean, besides me """

import random;

""" Help Menu print out"""

def printHelpMenu():
	print("Instructions of this program:\n");
	print("rand [a] [b]   Randomize the set of numbers of the main list, from [a] to [b]");
	print("set  [n]       Set [n] amount of numbers to be the size of the main list.\n");
	print("gen -s [n]     Generate a derivarive list from main, with items smaller than [n].");
	print("gen -e [n]     Generate a derivarive list from main, with items equal to [n].");
	print("geb -b [n]     Generate a derivarive list from main, with items bigger than [n].\n");
	print("sort sg        Sort the list from smaller to greatest number");
	print("sort gs        Sort the list from the greatest to smaller number\n");
	print("print main     Prints the main list.");
	print("print deri     Prints the derivative list\n");
	print("help           You get to see me once more.");
	print("exit           Exits the program.\n");
    
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

def askUserNumberInput(prompt):
    userInput = input(prompt);
    while (userInput.isdigit() == False):
        userInput = input("Not an integer, try again: ");
    return int(userInput);

def checkUserInputCommand(prompt):
    userInput = input(prompt);
    if (userInput.isdigit):
        return userInput;
    else:
        return None;


""" Program Methods """

def generateRandomNumbersForList(minRange, maxRange, mainList):
	if (len(mainList) != 0):
		for x in mainList:
			x = random.randrange(minimumRange, maximumRange);
	else:
		print("First, set an amount of numbers in the list, run 'set' command for this");
		


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

minimumRange = 0;
maximumRange = 1;

machineState = True;
while (machineState):
	
	command = processUserCommandLineInput("Exercise3@YourChoice~$ ");
	
	if (command[0] == "exit"):
		print("Bye bye.. :)");
		machineState = False;
		
	elif (command[0] == "help"):
		printHelpMenu();
		
	elif (command[0] == "rand"):
		random.seed();
		
		if (command[1] == None)
			minimumRange = askUserNumberInput("Specify minimum range for random number generation: ")
		else:
			minimumRange = command[1];
			
		if (command[2] == None)
			maximumRange = askUserNumberInput("Specify maximum range for random number generation: ")
		else:
			maximumRange = command[2];
		
		generateRandomNumbersForList(minimumRange, maximumRange, mainList);
			
		
	elif (command[0] == "set"):
		
		
	elif (command[0] == "bko"):
		printSecretScroll();
		
	else:
		print("Command not recognized");	
	
	
	"""	
	elif (command[0] == "gen"):
		
	
	elif (command[0] == "gen"):
		
	
	elif (command[0] == "gen"):
		
	
	elif (command[0] == "sort"):
		
	
	elif (command[0] == "print"):
		
	"""
	
	print(mainList);

"""

	I'm gonna pretend like I forgot to delete this just for effects
	
"""
