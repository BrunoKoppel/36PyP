# coding=utf-8
""" Wonder who reads these... I mean, besides me """

import random;

""" Help Menu print out"""

def printHelpMenu():
	print("Instructions of this program:\n");
	print("Avoid writing \"[\" or \"]\", these are used to determine where a certain placeholder is expected.")
	print("[main]:   The main list is the one that gets randomized and edited");
	print("[deri]:   The deri(vative) list gets generated using the 'gen' command.\n");
	print("rand [a] [b]    Randomize the set of numbers of the main list, from [a] to [b]");
	print("set  [n]        Set [n] amount of numbers to be the size of the main list.\n");
	print("gen -l [n]      Generate a derivarive list from main, with items lesser than [n].");
	print("gen -e [n]      Generate a derivarive list from main, with items equal to [n].");
	print("geb -g [n]      Generate a derivarive list from main, with items greater than [n].\n");
	print("sort [list] lg  Sort (main/deri) from lesser to greatest number");
	print("sort [list] gl  Sort (main/deri) from the greatest to lesser number\n");
	print("print [list]    Prints the (main/deri) list.\n");
	print("help            You get to see me once more.");
	print("exit            Exits the program.\n");
	
    
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


""" 

	Program Methods 

"""

def generateRandomNumbersForList(minRange, maxRange):
	return random.randrange(minimumRange, maximumRange);
		

def generateList(minRange, maxRange, mainList, numberInList):
	for x in range (0, numberInList):
		newNumber = random.randrange(minimumRange, maximumRange);
		mainList.append(newNumber);


def generateDerivedList(condition, number):
	temporalList = [];
	
	if (condition == "-l"):	
		for x in mainList:
			if (x < number):
				temporalList.append(x);
		
	elif (condition == "-e"):
		for x in mainList:
			if (x == number):
				temporalList.append(x);
				
	elif (condition == "-g"):
		for x in mainList:
			if (x > number):
				temporalList.append(x);
				
	elif (condition == None):
		print("You didn't enter a condition, check 'help' if you aren't sure.");
		
	else:
		print("Invalid command entered, check 'help' if you aren't sure.")
		
	return temporalList;
	
def sortList(listGiven, condition):
	
	if (condition == "lg"):
		for xIndex in listGiven:
			for yIndex in listGiven:
				if (yIndex < xIndex):
					listGiven[xIndex], listGiven[yIndex] = listGiven[yIndex], listGiven[xIndex]
				
	elif (condition == "gl"):
		for xIndex in listGiven:
			for yIndex in listGiven:
				if (yIndex > xIndex):
					listGiven[xIndex], listGiven[yIndex] = listGiven[yIndex], listGiven[xIndex]
		
	elif (condition == None):
		print("Condition not given");
	
	else:
		print("Condition not recognized");
	
	return listGiven;
	
""" 

	Welcome text 

"""

print("Welcome to the 3rd Exercise: ");
printHelpMenu();



""" 

	Variables for the list, and variables related to it 
	
"""

mainList = [];
mainListAmountOfNumber = 0;
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
		
		if (len(mainList) != 0):
			for index in mainList:
				mainList[index] = generateRandomNumbersForList(minimumRange, maximumRange);
		else:
			print("\nThe range of values is updated, but your list is empty.\nRun 'set' commmand, to set a size to it.\n\n");
		
	elif (command[0] == "set"):
		if (command[1] > 0):
			for index in range(0, command[1])
			mainList[index] = generateRandomNumbersForList(minimumRange, maximumRange);
		else:
			print("Error, value is zero or below.");
			
	elif (command[0] == "gen"):
		derivedList = generateDerivedList(command[1], command[2]);
		
	elif (command[0] == "sort"):
		if (command[1] == "main"):
			mainList = sortList(mainList, command[2]);
			
		elif (command[1] == "deri"):
			derivedList = sortList(derivedList, command[2]);
			
		elif (command[1] == None):
			print("List not recognized");
			
		else:
			print("List not given");	
		
	elif (command[0] == "bko"):
		printSecretScroll();
		
	else:
		print("Command not recognized");	
	
	
	"""	
	
	elif (command[0] == "print"):
		
	"""
	
	print(mainList);

"""

	I'm gonna pretend like I forgot to delete this,
		your truly,
			bko
	
"""
