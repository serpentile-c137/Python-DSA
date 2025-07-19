from math import sqrt
def divisors(num):
    if num < 0: 
        return "Input must be a non-negative integer."
    divs = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            divs.append(i)
            if i != num // i:
                divs.append(num // i)
    divs.sort()
    return divs

print(divisors(20))  # [1, 2, 4, 5, 10, 20]
print(divisors(15))  # [1, 3, 5, 15]
print(divisors(1))   # [1]
print(divisors(-10))   # [1] (0 is conventionally considered to