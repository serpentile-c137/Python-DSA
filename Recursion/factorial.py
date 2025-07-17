def factorial(n):
    assert n >= 0 and int(n) == n, "n must be a non-negative integer"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
    
print(f"Factorial of 5 is: {factorial(5)}")