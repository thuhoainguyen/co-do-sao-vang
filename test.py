# Lesson_1: Variables and String Format
print("Welcome to Python class")

num_1 = 1.2
num_2 = 2
print("Sum of", num_1, "and", num_2, "is", num_1 + num_2)

sum = num_1 + num_2
print(f"The sum of {num_1} and {num_2} is {sum}")

# Lesson_2: Data types
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

# Lesson_3: Conditional Statements 

# Ex.1: Write a program that asks the user to enter a number and prints out whether it is even or odd. 
# (Assume that the user can only enter integers)

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Ex.2: Write a program that simulates a traffic light sequence based on a given signal.
# The valid inputs are 'red', 'yellow', and 'green'. The program should print out the next signal.
# For example, if the user enters 'red', the program should print out 'green'.
# If input is not valid, the program should print out 'invalid input'.

# input("Enter a traffic signal (green, yellow, red):")
# if input == "green":
#     print("yellow")
# elif input == ""



