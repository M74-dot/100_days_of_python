# List Comprehension

numbers = [1,2,3]
new_list = [num+1 for num in numbers]
# print(new_list)

name = "Manisha"
new_list = [letter for letter in name]
# print(new_list)

new_list = [i * 2 for i in range(1, 5)]
# print(new_list)

# Conditional List Comprehension

names = ["Manisha", "Vidisha", "Monika", "Kshitija", "Prachi"]
short_names = [name for name in names if len(name) == 6]
# print(short_names)

names = ["Manisha", "Vidisha", "Monika", "Kshitija", "Prachi"]
short_names = [name.upper() for name in names if len(name) > 6]
# print(short_names)


# QUIZ 1
numbers = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [num*num for num in numbers]
# print(squared_numbers)

# QUIZ 2
# list_of_strings = input().split(',')
# print(list_of_strings)
# list_of_int = [int(num) for num in list_of_strings]
# print(list_of_int)
# even_nums = [num for num in list_of_int if num%2==0]
# print(even_nums)

# QUIZ 3
with open("file1.txt") as file1:
    list1 = file1.readlines()
    list1 = [num.strip() for num in list1]

with open("file2.txt") as file2:
    list2 = file2.readlines()
    list2 = [num.strip() for num in list2]

result = [int(num) for num in list1 if num in list2]
print(result)