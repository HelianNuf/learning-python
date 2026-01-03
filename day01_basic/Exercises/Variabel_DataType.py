## Variabel and Data Type + trying input
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
