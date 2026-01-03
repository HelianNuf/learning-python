# The basic login system uses logical operators

user = input("Username: ")
pw = input("Password: ")

if user == "admin" and pw == "123":
    print("Login Success")
else:
    print("input invalid")