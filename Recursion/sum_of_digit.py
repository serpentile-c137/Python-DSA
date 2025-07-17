def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "n must be a non-negative integer"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n // 10))
    
n = 1111111
print(f"The sum of digits in {n} is: {sumOfDigits(n)}")