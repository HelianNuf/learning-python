# Basic Function

def say_hi():
    print ("Hello World\n")

say_hi()

# Paramater function

def data(name, age):
    print(f"Nama: {name}")
    print(f"Age: {age}")

data("Nur Fadhilah", 20)

# Return function

def data_rect(long, wide):
    rectangle = long*wide
    print(f"\nArea of ​​the rectangle: {rectangle}")
    return rectangle

data_rect(4,5)
