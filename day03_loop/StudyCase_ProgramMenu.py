# Study Case : Basic Program Menu

# Chosing menu; 
# (1) Showing numbers 1-5, 
# (2) Showing even numbers 1-10
# (3) Close program

print("=== MENU ===")
print("""1. Showing numbers 1-5, 
2. Showing even numbers 1-10
3. Close program\n""")

while True:
    try:
        choice = int(input("Select Menu (1/2/3): "))
        print("...")
        if choice == 1:
            for i in range(5):
                i += 1
                print(i)
        elif choice == 2:
            number = 0
            while number < 10:
                number += 1
                if number % 2 == 0:
                    print(number)
        elif choice == 3:
            break
        else:
            print("Input Error: Input invalid, please select menu (1/2/3).")
            continue
    except ValueError:
        print("Input Error: Input invalid, please select numbers.")
        continue
    break
print("...")
print("Program Completed")