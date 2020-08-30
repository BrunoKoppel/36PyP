def askName():
    name = input("Hello what's your name? ");
    return name;

def askAge():
    age = int(input("and what's your age? " ));
    return age;

def calculateYear(age):
    year = 2020 + (100 - age);
    return year;

def askLinesToPrint():
    linesToPrint = int(input("What your favorite number? "));
    return linesToPrint;

def printInformation(name, age, linesToPrint):
    year = calculateYear(age);
    for x in range(0, linesToPrint):
        print("Hello " + name + " I know you are " + str(age) + " years old now but you will be a 100 year old in " + str(year));

printInformation(askName(), askAge(), askLinesToPrint());


