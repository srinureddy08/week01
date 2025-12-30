# create  list on grades
grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]

count_A = 0
count_B = 0
count_C = 0
count_below_70 = 0

for grade in grades:
    if grade >= 90:
        count_A += 1
    elif grade >= 80:
        count_B += 1
    elif grade >= 70:
        count_C += 1
    else:
        count_below_70 += 1

print("Number of students with A (≥90):", count_A)
print("Number of students with B (80–89):", count_B)
print("Number of students with C (70–79):", count_C)
print("Number of students below 70:", count_below_70)
