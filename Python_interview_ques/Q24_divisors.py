def divisors(num): # brute force
    if num < 0: 
        return "Input must be a non-negative integer."
    divs = []
    for i in range(1, num + 1):
        if num % i == 0:
            divs.append(i)
    return divs

print(divisors(10))  # [1, 2, 5, 10]
print(divisors(15))  # [1, 3, 5, 15]
print(divisors(1))   # [1]
print(divisors(-10))   # [1] (0 is conventionally considered to