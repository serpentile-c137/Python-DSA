# Explain Difference Between is vs == Operator


# What it Does
# == : Compares values
# is : Compares identities (memory address)

# Example:

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b : ", a == b)  # True, because values are the same
print("a is b : ", a is b)  # False, because a and b are different objects in memory