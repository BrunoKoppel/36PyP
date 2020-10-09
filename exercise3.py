# coding=utf-8

def printHelpMenu():
	print("Instructions of this program:\n");
	print("-rand [n]   Randomize the set of numbers of the main list, with [n] as the maximum possible value for any number");
	print("-set  [n]   Set [n] amount of numbers to be the size of the main list.\n");
	print("-cs [n]   create a derivarive list from main, with items smaller than [n].");
	print("-ce [n]   create a derivarive list from main, with items equal to [n].");
	print("-cb [n]   create a derivarive list from main, with items bigger than [n].\n");
	print("-so sg    Sort the list from smaller to greatest number");
	print("-so gs    Sort the list from the greatest to smaller number\n");
	print("-pr main  Prints the main list.");
	print("-pr deri  Prints the derivative list\n");
	print("-he       You get to see me once more.");
	print("-ex       Exits the program.\n");
    
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

print("Welcome to the 3rd Exercise: ");
printHelpMenu();

machineState = True;
while (machineState):
	
	command = processUserCommandLineInput("Exercise3@YourChoice~$ ");
	
	print(command[0]);
	
	if (command[0] == "-ex"):
		print("Bye bye.. :)");
		machineState = False;
	
	elif (command[0] == "-he"):
		printHelpMenu();
		
	elif (command[0] == "bko"):
		printSecretScroll();
	
	else:
		print("Command not recognized");	
	



"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [];



	for x in range(len(a)):
		if (a[x] < 5):
			b.append(a[x]);

	print(b);
	
"""
