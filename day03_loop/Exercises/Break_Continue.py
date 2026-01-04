# Loop numbers 1-10
# if number 3 -> continue and is number 7 -> break

number = 0

while number < 10:
    number += 1
    if number == 3:
        continue
    elif number == 7:
        break
    print(number)
print("Loop stopped at", number)