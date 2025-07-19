def check_palindrome(n):
    num = n
    res = 0
    while num > 0:
        last = num % 10
        res = (res * 10) + last
        num //= 10
    return res == n

print(check_palindrome(12321))  # True
print(check_palindrome(1234))  # False