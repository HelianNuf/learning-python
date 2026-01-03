# Study Case: Determine student grades based on final grades.

# Input: final_score (0–100)
# Output: grade (A/B/C/D)

print("=== HASIL PENILAIAN ===")
score = int(input("Final Score: "))

if score >= 85:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 65:
    grade = "C"
else:
    grade = "D"

print("Grade :", grade)

