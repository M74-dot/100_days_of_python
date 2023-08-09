def prime_checker(number):
    if number < 2:
        return "It's not a Prime Number"
    i = 2
    while i * i <= n:
        if n % i == 0:
            return "It's not a Prime Number"
        i += 1
    return "It's a Prime Number"


n = int(input('Wnter a number you want to check '))
print(prime_checker(n))