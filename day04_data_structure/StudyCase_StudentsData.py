# Study Case : Students Data Management
# Program save and show the students data.

# List to accommodate many students
data = []

# Student data using Dictionary
student1 = {
    "nim": (12345,), # Tuple (NIM do not change)
    "name": "nana",
    "age": 20
}

student2 = {
    "nim": (12346,),
    "name": "budi",
    "age": 21
}


data.append(student1)
data.append(student2)

print("=== STUDENTS DATA ===")
for mhs in data:
    print(f"NIM   : {mhs['nim'][0]}")
    print(f"Name  : {mhs['name']}")
    print(f"Age  : {mhs['age']}")
    print("-" * 20)
