student_heights = input("Input a list of students heights ").split(" ")

for i in range(0, len(student_heights)-1):
    student_heights[i] = int(student_heights[i])

# print(student_heights)

sum = 0
for i in range(0, len(student_heights)-1):
    sum += student_heights[i]

avg = sum / len(student_heights)
print(avg)
