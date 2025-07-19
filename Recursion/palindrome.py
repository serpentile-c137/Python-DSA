def check_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return check_palindrome(s, left + 1, right - 1)

s = "anbcddcbna"
left = 0
right = len(s) - 1
print(check_palindrome(s, left, right))