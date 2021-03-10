def askName():
	name = input("\n\nHello what's your name? ");
	return name;

def askAge():
	age = input("What's your age? " );
	if (age.isdigit()):
		return int(age);
	else:
		return 100;

def calculateYear(age):
	year = 2020 + (100 - age);
	return year;

def askLinesToPrint():
	linesToPrint = input(",and what your favorite number? (BEWARE: keep it small) ");
	if (linesToPrint.isdigit()):
		return int(linesToPrint);
	else:
		return 1;

def printInformation(name, age, linesToPrint):
	year = calculateYear(age);
	print("\n");
	for x in range(0, linesToPrint):
		if (age < 40):
			print("Hello " + name + ", I know you are " + str(age) + " years old, now, BUT, you will be a 100 year old! in " + str(year) + ". Better make the BEST of what is left, in the CYBERPUNK WORLD!!!");
		elif (age >= 40 and age < 100):
			print("Hello " + name + ", I know you are " + str(age) + " years old, now, BUT, you will be a 100 year old! in " + str(year) + ". Better make the BEST of what is left!");
		else:
			print("Hello " + name + ", It seems like you are " + str(age) + " years old by " + str(year) + ". Congrats on getting so far!!");

def askUserToContinue():
	command = str(input("\nDo you want to introduce yourself again? (Yes/No):  "))
	if (command == "Yes" or command == "Y" or command == "y"):
		return True;
	elif (command == "No" or command == "N" or command == "n"):
		print("Bye bye :)");
		return False;
	else:
		print("I didn't catch that...");
		return askUserToContinue();

machineState = True;
while (machineState):
	printInformation(askName(), askAge(), askLinesToPrint());
	
	machineState = askUserToContinue();
