def power(base, exp):
    assert int(exp) == exp, "exp must be a non-negative integer"
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / base * power(base, exp + 1)
    else:
        return base * power(base, exp - 1)
    

base = 4
exp = -1
print(f"{base} raised to the power of {exp} is: {power(base, exp)}")