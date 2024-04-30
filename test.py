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

# name = input("Enter your name: ")
# while name != "Tu":
#     name = input("Enter your name: ")
# else:
#     print("Found Tu !")

print("-----------------------------------------------------------------")

# For loop:
# Syntax:
# for <variable> in <iterable>:
#  <code>

# for i in range(5):
#   print(i)

# for i in range(5, 10):
#   print(i)

# for i in range (5, 10, 2):
#   print(i)

# fruits = ['apple', 'banana', 'lemon', 'pineapple', 'opa']
# for i in range(0, len(fruits) , 2):
#   print(f'Thu likes {fruits[i]}')

# stmt = "Thu likes lemon"
# word = ''
# words = []
# for a in stmt:
#     if a != ' ':
#         word = word + a
#     else:
#         words.append(word)
#         word = ''
# words.append(word)
# print(words)
# dna = "cgagagacgatcgatgc"  # sort out "tcg"
# print(dna.find("tcg"))
# print(dna[0, 10 ])



# output: ["cga", "atgc"]
# stmt = "Thu likes lemon"
# words = stmt.split(' ')
# for word in words:
#     print(word)
        



# Ex.1: Count how many times 'e' appears in the following string 'Thu likes lemon'
# stmt = 'Thu likes lemon'
# i = 0
# for a in stmt:
#     if a == 'e':
#         i = i + 1
# print(i)
print("-----------------------------------------------------")

# Ex.2: Count how many times 0 and 1 appear in the following list [0, 1, 0, 1, 1, 0, 0, 1, 0]
print("Lesson 4: Loops")
print("Ex2")
binary_list = [0, 1, 0, 1, 1, 0, 0, 1, 0]
i = 0
j = 0
for a in binary_list:
    if a == "0":
        i = i + 1
    else:
        j = j + 1
print(f"0 appears {i} times")
print(f"1 appears {j} times")

# Ex.3: # Write a program that asks the user to enter a number and prints out the sum of all numbers from 0 to the entered number

# Ex.4: Write a program that asks the user to enter a number and prints out the sum of all even numbers from 0 to the entered number

# Ex.5: # Write a program that asks the user to enter a number until the user enters 0. The program then calculates:
# - The total number
# - The total number of positive numbers
# - The total number of negative numbers
# - The sum of all numbers
# - The average of all numbers

# Ex.6: Write a program that asks the user to enter a number and prints out whether it is a prime number or not. (Assume that the user can enter any number)

# Ex.7: Write a program that asks the user to enter a number and check if the number is a square number or not. (Assume that the user can enter any number)

# Ex.8: Write a program that asks the user to enter a number and prints out the factorial of that number. (Assume that the user can enter any integers)
# Note that factorial of negative numbers exists but is not valid for this exercise.
# But if you are good, try to do it.

# Ex.9: Write a program that asks the user to enter a number and prints out the Fibonacci sequence up to that number. (Assume that the user can enter any integers)


