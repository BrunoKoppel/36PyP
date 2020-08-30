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


machineState = True;
divisionLoop = True;
check = None;
print("Hello! Welcome to the Odd or Even Application");
while(machineState):
    
    print("Please select a command:");
    print("a: Enter new check value");
    print("b: Divide the numbers.");
    print("q: to quite the program.\n");
    command1 = input("Your input: ");
    

    if(command1 == "a"):
        
        check = int(input("Enter new check number: "));
        print("\n");

    elif(command1 == "b"):
        divisionLoop = True;
        
        if(check == None):
            check = checkUserInput("Please set a value for the check number: ");
            
        while(divisionLoop):
            command2 = input("Enter number to divide number (Or any character to exit): ");
            
            if(command2.isdigit()):
                num = int(command2);
                
                if ((num % check) == 0):
                    print("YES!!! The number " + str(num) + " is divisible by " + str(check) + "\n");

                else:
                    print("NOO!! :( The number " + str(num) + " is not divisible by " + str(check) + "\n");
                    
                print("ENTER ANY CHARACTER TO STOP CHECKING DIVISIONS FOR " + str(check) + "\n");

            else:
                divisionLoop = False;
            
    elif(command1 == "q"):
        
        machineState = False;
            
    elif(command1 == "bko"):
        print("easter bugs make me strong... meow");
        print("- -- .-.");
        print("- - /  |                - - /|_/|      .-------------------.");
        print("   /   |  - _______________| @.@|     /    Bruno Köppel     )");
        print("- |    |-- (______         >\_C/< ---/                     /");
        print("  |    |  -  -   / ______  _/____)  (   Brunokoppel.com   /");
        print("-- \   | -  -   / /\ \   \ \         `-------------------'");
        print(" -  \  |     - (_/  \_) - \_)");
        print("- -  | |\n\n");
        
    else:
        
        print("You have entered the wrong command please try again...");