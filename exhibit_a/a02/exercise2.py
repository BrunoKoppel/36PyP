# coding=utf-8

def checkUserInput(prompt):
	userInput = input(prompt);
	while (userInput.isdigit() == False):
		userInput = input("Sorry try again, " + prompt);
	print("\nYour input is " + userInput + "\n");
	return int(userInput);

def checkUserInputCommand(prompt):
	userInput = input(prompt);
	if (userInput.isdigit):
		print("\nYour input is " + userInput + "\n");
		return userInput;
	else:
		return None;
	
def printHelpMenu():
	print("Instructions of this program:");
	print("-a: Enter new check value");
	print("-b: Divide the numbers.");
	print("-h: You get to see me once more.\n");
	print("-q: Quits the program.\n");

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


machineState = True;
divisionLoop = True;
check = None;
print("Hello! Welcome to the 2nd Exercise!");
printHelpMenu();

while(machineState):
	command1 = str(input("Exercise2@YourChoice~$ "));


	if(command1 == "-a"):

		check = checkUserInput("Enter new check number: ");
		print("\n");

	elif(command1 == "-b"):
		divisionLoop = True;
	
		if(check == None):
			check = checkUserInput("Please set a value for the check number: ");

		while(divisionLoop):
			command2 = input("Enter number to divide number (Or any character to exit): ");
			
			if(command2.isdigit()):
				num = int(command2);
				
				if ((num % check) == 0):
					print("\nYES!!! " + str(num) + " is divisible by " + str(check) + "\n");

				else:
					print("\nNO " + str(num) + " is not divisible by " + str(check) + "\n");
					
				print("Enter a non numberic charater to stop division for " + str(check) + "\n");

			else:
				divisionLoop = False;

	elif(command1 == "-h"):
		printHelpMenu();
	
	elif(command1 == "-q"):
		machineState = False;
	
	elif(command1 == "bko"):
		printSecretScroll();
	
	else:
	
		print("Command Invalid");
