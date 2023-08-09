import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z' 
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']

print("Welcome to the PyPassword Generator!")
no_of_letters = int(input("How many letters would you like in your password\n"))
no_of_numbers = int(input("How many numbers would you like\n"))
no_of_symbols = int(input("How many symbols would you like\n"))


# Easy Level
# password = ''
# for i in range(no_of_letters):
#     random_letter = random.choice(letters)
#     password += random_letter
# for i in range(no_of_numbers):
#     random_no = random.choice(numbers)
#     password += random_no
# for i in range(no_of_symbols):
#     random_symbol = random.choice(symbols)
#     password += random_symbol

# print(password)


# Hard Level
password_list = []
for i in range(no_of_letters):
    password_list.append(random.choice(letters))

for i in range(no_of_numbers):
    password_list.append(random.choice(numbers))

for i in range(no_of_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ''
for char in password_list:
    password += char
print(password)
