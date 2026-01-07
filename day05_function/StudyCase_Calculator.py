# Study Case: Basic Calculator
# Show basic operation (-, +, x, :)

print("\n=== Calculator ===")
while True:
    try:
        def Sum(a, b):
            sum_ = a+b
            return(sum_)

        def subtraction(a, b):
            subtraction_ = a-b
            return(subtraction_)

        def multiplication(a, b):
            multiplication_ = a*b
            return(multiplication_)

        def division(a, b):
            division_ = a/b
            return(division_)

        num_1 = int(input("\nInput number: "))
        num_2 = int(input("Input another number: "))

        print("\n1. Sum")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        operation = int(input("\nInput your operation (1/2/3/4): "))

        if operation == 1:
            print("\n----------")
            print(f"{num_1} + {num_2}")
            print("=", Sum(num_1, num_2))
            print("----------")
        elif operation == 2:
            print("\n----------")
            print(f"{num_1} - {num_2}")
            print("=",subtraction(num_1, num_2))
            print("----------")
        elif operation == 3:
            print("\n----------")
            print(f"{num_1} x {num_2}")
            print("=", multiplication(num_1, num_2))
            print("----------")
        elif operation == 4:
            print("\n----------")
            print(f"{num_1} : {num_2}")
            print("=", division(num_1, num_2))
            print("----------")
        else:
            print("Input Error: Select the available menu!")
            continue
        
        while True:
            question = input("Want to do another calculation? (y/n) :")
            if question == "y":
                break
            elif question == "n":
                exit()
            else:
                print("Input Error: Please enter 'y' or 'n'")
                continue
    except ValueError:
        print("Input Error: Enter only numbers")
        
