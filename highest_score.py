scores = input("Input a list of students scores ").split(" ")

for i in range(0, len(scores)):
    scores[i] = int(scores[i])

print(scores)

max_score = scores[0]
for i in range(1, len(scores)):
    if scores[i] > max_score:
        max_score = scores[i]

print(f"The highest score in the class is: {max_score}")
