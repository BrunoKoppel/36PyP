# coding=utf-8
""" Wonder who reads these... I mean, besides me """

import random;

""" Help Menu print out"""

def printHelpMenu():
	print("Instructions of this program:\n");
	print("rand [a] [b]   Randomize the set of numbers of the main list, from [a] to [b]");
	print("set  [n]       Set [n] amount of numbers to be the size of the main list.\n");
	print("cs [n]         create a derivarive list from main, with items smaller than [n].");
	print("ce [n]         create a derivarive list from main, with items equal to [n].");
	print("cb [n]         create a derivarive list from main, with items bigger than [n].\n");
	print("so sg          Sort the list from smaller to greatest number");
	print("so gs          Sort the list from the greatest to smaller number\n");
	print("pr main        Prints the main list.");
	print("pr deri        Prints the derivative list\n");
	print("he             You get to see me once more.");
	print("ex             Exits the program.\n");
    
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

def generateRandomNumbers(minRange, maxRange, )


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
	
	if (command[0] == "ex"):
		print("Bye bye.. :)");
		machineState = False;
		
	elif (command[0] == "he"):
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
		
		if (len(mainList) != 0):
			for x in mainList:
				x = random.randrange(minimumRange, maximumRange);
				
		else:
			print("First, set an amount of numbers in the list, run 'set' command for this");
		
	elif (command[0] == "set"):
		
		
	elif (command[0] == "bko"):
		printSecretScroll();
		
	else:
		print("Command not recognized");	
	
	
	"""	
	elif (command[0] == "cs"):
		
	
	elif (command[0] == "ce"):
		
	
	elif (command[0] == "cb"):
		
	
	elif (command[0] == "so"):
		
	
	elif (command[0] == "pr"):
		
	"""
	
	print(mainList);

"""

	I'm gonna pretend like I forgot to delete this just for effects
	
"""
