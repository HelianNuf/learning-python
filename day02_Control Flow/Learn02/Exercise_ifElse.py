# If, elif, else & 
print("=== IF, ELIF, ELSE ===")

age = int(input("Input your age: ")) # need to casting data type to int cause input is str

if age < 18:
    print("Age category: Child")
elif age > 18 & age < 25:
    print("Age category: Teenager")
else:
    print("Age category: Adult\n")

# Comparison Operators
print("=== COMPARISON OPERATORS ===")

a = 10
b = 3

print("A =", a)
print("B =", b)

print("\n- Apakah nilai variabel A lebih besar dari nilai B?", a > b)
print("- Apakah nilai variabel B lebih besar sama dengan A?", b >= a)
print("- Apakah nilai variabel A sama dengan B?", a == b)
print("- Apakah nilai variabel A tidak sama dengan B?", a != b)

# Logical Operators
print("=== LOGICAL OPERATORS ===")

score = int(input("input your score : "))
presence = input("are you present (y/n)? ")

print("\nStatus passed:", score >= 75 and (presence == "y" or presence == "yes")) #besides "and" and "or" there is also "not"