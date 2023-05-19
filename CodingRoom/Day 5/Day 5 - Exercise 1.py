# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

TotalHeight = 0
TotalStudent = 0
for student_height in student_heights:
    TotalHeight = TotalHeight + student_height
    TotalStudent = TotalStudent + 1

avgHeight = int(round(TotalHeight/TotalStudent,0))
print(avgHeight)