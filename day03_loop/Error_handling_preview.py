# Basic error handling preview
# Used to support case study stability

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Invalid input. Please enter a number.")