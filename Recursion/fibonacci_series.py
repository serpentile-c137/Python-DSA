def fibonacci(n):
    assert n >= 0 and int(n) == n, "n must be a non-negative integer"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci of 8 is: {fibonacci(8)}")