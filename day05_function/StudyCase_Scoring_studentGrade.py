# Study Case: Scoring final grade students
# Calculate the final grades using a function

# function: average score and determine grades

print("Input your score.. (1-100)")

while True:    
    try:
        exercise = int(input("\nExercise: "))
        middle_exam = int(input("Middle Exam: "))
        final_exam = int(input("Final Exam: "))

        if exercise <= 100 and middle_exam <= 100 and final_exam <= 100:
            break
        else:
            print("\nInput Error: Please input scores 1-100!")
    except ValueError:
        print(("\nInput Error: Please input the numbers 1-100!"))
        continue

def Average():
    score = (exercise + middle_exam + final_exam)/3
    return(score)

final_score = Average()

def Grade(score):
    if score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    elif score >= 40:
        print("Grade: D")
    else:
        print("Grade: E")

print("\n=== RESULT GRADES ===")
print("Final Score:", final_score)
Grade(final_score)