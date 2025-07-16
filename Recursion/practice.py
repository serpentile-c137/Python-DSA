def recursionMethod(n):
    print(f"calling recursionMethod({n})")
    if n < 1:
        print("n is less than 1, returning...")
    else:
        recursionMethod(n - 1)
        print(f"Current value of n: {n}")

if __name__ == "__main__":
    n = 5
    print(f"Starting recursion with n = {n}\n")
    recursionMethod(n)
    print("\nRecursion completed.")