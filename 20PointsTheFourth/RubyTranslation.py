import os

def menu():
  menu_string = "1. Show Menu \n"
  menu_string += "2. Add Numbers \n"
  menu_string += "3. Subtract Numbers\n"
  menu_string += "4. Quit\n"
  return menu_string

os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

choice = 0
while choice < 4:
  print(menu())
  choice = int(input())  # Get user input and convert to integer
  if choice == 1:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
  elif choice == 2:
    print("\n\nAdd some numbers \n\n")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum is: {result}")
  elif choice == 3:
    print("\n\nSubtract some numbers\n\n")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"The difference is: {result}")
  else:
    pass  # Do nothing for other choices
