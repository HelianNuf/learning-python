# If, elif, else & 
print("=== IF, ELIF, ELSE ===")

age = int(input("Input your age: ")) # need to casting data type to int cause input is str

if age < 18:
    print("Age category: Child")
elif age > 18 & age < 25:
    print("Age category: Teenager")
else:
    print("Age category: Adult\n")
