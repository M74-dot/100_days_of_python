import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# # print(names)
# count = len(names)
# person_who_will_pay = random.randint(0, count-1)

person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to pay the bill")

# print(names[person_who_will_pay] + " is going to pay the bill.")
