def gcd(a, b):
    assert int(a) == a and int(b) == b, "Both inputs must be integers"
    a, b = abs(a), abs(b)  # Ensure inputs are non-negative
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
a = -48
b = 18
print(f"GCD of {a} and {b} is: {gcd(a, b)}")