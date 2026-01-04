# Study Case : Guess The Number

try:
    for i in range(20):
        input_ = int(input("Select Numbers (1-100): "))
        number = 17
        if input_ == 17:
            print("You got the number")
            break
        elif input_> 100 or input_ < 1 :
            print("Select numbers 1-100!")
            print("-----")
        else:
            print("Try Again..")
            print("-----")
        
except ValueError:
    print("Input Error: Please select the number. Try again later.")

