
# Basic print
print("Hello, Python!")

# Separating print sentences 
print("""\nMy name is Nur Fadhilah
I'm 20
\nLet's get started..\n""")

## Variabel and Data Type
print("=== Variabel and Data Type ===")
name = "Nur Fadhilah"
age = 20
bmi =  19.10
student = True

print("Name =", name,", Data type =", type(name))
print("Age =", age,", Data type =", type(age))
print("BMI =", bmi,", Data type =", type(bmi))
print("Student =", student,", Data type =", type(student))

bmi =  19.14  # New data
print("\nNew BMI =", bmi)


name = input("\nMasukan nama = ") # Input (value input is string even you input the number)
print("New name =", name) # New data from input


## Math Basic Operation
print("=== Basic Operation ===")

a = 20
b = 5

print("\nfirst num :", a)
print("second num :", b)

print("\nsum :", a + b)
print("subtraction :", a - b)
print("multiplication :", a * b)
print("division :", a / b)
print("modulus :", a % b)
print("exponent :", a ** b)
print("integer division :", a // b)
