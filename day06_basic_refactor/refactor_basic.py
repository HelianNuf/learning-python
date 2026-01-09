# ======================
# DAY 1
# ======================

# print & input
name = input("Input your name: ")
print("Hello,", name)

# Variables & Data Types
age = 20          # int
height = 160.5     # float
active = True       # boolean
hobby = "Reading Book"   # string

# Basic Arithmetic Operations
a, b = 10, 3
print(a + b)   # sum
print(a - b)   # subtract
print(a * b)   # multiply
print(a / b)   # divide


# ======================
# DAY 2
# ======================

score = 85

# If, elif, else
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"

print("Grade:", grade)

# Comparison & Logical Operators
age = 18
have_ID_Card  = True

if age >= 17 and have_ID_Card:
    print("Can make a driving license")


# ======================
# DAY 3
# ======================

# For Loop
for i in range(3):
    print("For loop:", i)

# While Loop
count = 0
while count < 3:
    print("While loop:", count)
    count += 1

# Break & Continue
for i in range(5):
    if i == 3:
        break
    if i == 1:
        continue
    print("Numbers:", i)


# ======================
# DAY 4
# ======================

# List
fruits = ["appel", "banana", "cherry"]
fruits.append("pear")

# Set
unique_numbers = {1, 2, 2, 3}

# Tuple
coordinate = (10, 20)

# Dictionary
Student = {
    "name": "Ani",
    "age": 20
}

print(fruits)
print(unique_numbers)
print(coordinate)
print(Student["name"])


# ======================
# DAY 5
# ======================

# Basic Function
def say_hi():
    print("Hello!")

# Function with Parameter
def hi_with_name(name):
    print("Hello,", name)

# Function with Return
def sum(a, b):
    return a + b

say_hi()
hi_with_name("Budi")
value = sum(5, 3)
print("Value:", value)
