# new_dict = {new_key:new_value for (key,values) in dict.items() if test}
 
import random
names = ["Manisha", "Vidisha", "Monika", "Kshitija", "Prachi"]
students_score = {student:random.randint(1,100) for student in names}
# print(students_score)

passed_students = {student:mark for student,mark in students_score.items() if mark >=50}
# print(passed_students)


# QUIZ 1
# sentence = input()

# result = {word:len(word) for word in sentence.split()}
# print(result)

# QUIZ 2
# weather_c = eval(input())
# # print(weather_c)

# weather_f = {day:temperature * 9/5 + 32 for day,temperature in weather_c.items()}
# print(weather_f)


