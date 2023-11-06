
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

continue_or_not = True
while(continue_or_not):
    num1 = int(input("What's the first number?: "))
    num2 = int(input("What's the second number?: "))
    for op in operations:
        print(op)
    operation = input("Pick an operation from from the line above: ")


    function = operations[operation]
    result = function(num1, num2)

    print(f"{num1} {operation} {num2} = {result}")

    operation = input("Pick another operation: ")
    num3 = int(input("What's the next number?: "))
    calc_fun = operations[operation]
    result2 = calc_fun(result, num3)
    print(f"{result} {operation} {num3} = {result2}")
    choice = input("Do you wanna continue? Type 'y' to continue 'n' to exit ").lower()

    if choice=='n':
        continue_or_not = False
