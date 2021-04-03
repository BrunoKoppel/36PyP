import os

booklist = {
  "1":"a01/exercise1.py",
  "2":"a02/exercise2.py"
}

def askUserToInputProgramToRun():
  command = str(input("\n(Enter Number) "))
  os.system("sudo python ./" + booklist.get(command))

print("Welcome to Python Code Vault!")
print("Choose a program to run:")
print("1. Inputs")
print("2. Odd or Even")
print("3. List less than x")
askUserToInputProgramToRun()
