# Logical Operators
print("=== LOGICAL OPERATORS ===")

score = int(input("input your score : "))
presence = input("are you present (y/n)? ")

print("\nStatus passed:", score >= 75 and (presence == "y" or presence == "yes")) 