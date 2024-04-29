# Lesson_1: Variables and String Format
print("Lesson 1: ")
print("Welcome to Python class")

num_1 = 1.2
num_2 = 2
print("Sum of", num_1, "and", num_2, "is", num_1 + num_2)

sum = num_1 + num_2
print(f"The sum of {num_1} and {num_2} is {sum}")

print("-----------------------------------------------")

# Lesson_2: Data types
print("Lesson 2: Data types")
var_integer = 2
var_float = 5.5
var_string = "cafe"
var_boolean = True
var_tuple = (var_integer, var_float, var_string, var_boolean)
var_tuple = (3, 5.5, "cafe", False)

var_list = [1, 2, 'c', 4, 5]
print(f"Third element of the list: {var_list[2]}")
print(f"Size of the list: {len(var_list)}")

var_dict = {"name": "AnhTu", "age": 27, "is_student": False}
print(f"Name: {var_dict['name']}, age: {var_dict['age']}, is student: {var_dict['is_student']}")

print("-----------------------------------------------")

# Lesson_3: Conditional Statements 
print("Lesson 3: Conditional Statements")

# Ex.1: Write a program that asks the user to enter a number and prints out whether it is even or odd. 
# (Assume that the user can only enter integers)
print("Ex1: Even/Odd number")

prompt = "Enter a number: "
# num = int(input(prompt))
num = 6
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("-----------------------------------------------")

# Ex.2: Write a program that simulates a traffic light sequence based on a given signal.
# The valid inputs are 'red', 'yellow', and 'green'. The program should print out the next signal.
# For example, if the user enters 'red', the program should print out 'green'.
# If input is not valid, the program should print out 'invalid input'.

# Ex.3: Extension to Ex.2 but to make it more challenging, the program should 
# assist the user by allowing case insensitive input.
# For example, if the user enters 'RED' or 'Red', the program should accept it.

print("Ex2: ")

# light = input("Enter a traffic signal (green, yellow, red): ")
# light = light.lower()
light = "green"
if light == "green":
    print("yellow")
elif light == "yellow":
    print("red")
elif light == "red":
    print("green")
else:
    print("invalid input")

print("------------------------------------------------------")

# Loop: for loop and while loop
# While loop:
print("Lesson 4: Loops")
# Syntax:
# while <condition>:
#   <code>
print("Ex1: While loop with count")
count = 0
while count < 5:
  print(count)
  count = count + 1

# Spot the bug in the following code
# Then fix the bug
print("Ex2: Break the loop")
name = 'Thu'
while name == 'Thu':
    print('Hello Thu')
    break

name = 'Thu'
while name == 'Thu':
    print('Hello Thu')
    name = "Tu"

# Write a program that ask the user to type their name.
# If the user's name is not "Tu", the program will keep asking the user to type their name.
# When the user types "Tu", the program will print out "Found Tu" and stops.

name = input("Enter your name: ")
while name != "Tu":
    name = input("Enter your name: ")
else:
    print("Found Tu !")


