# List Comprehension vs Generator Expression

# List Comprehension
arr = [x**2 for x in range(10)]
print("List Comprehension:", arr)

# Generator Expression
gen = (x**2 for x in range(10))
print("Generator Expression:", gen)

# output:

# List Comprehension: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Generator Expression: <generator object <genexpr> at 0x101084d40>