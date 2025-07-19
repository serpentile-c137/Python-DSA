def palindrome(s):
    left = 0
    right  = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "racecar"
print(f"Is '{s}' a palindrome? {palindrome(s)}")
s = "hello"
print(f"Is '{s}' a palindrome? {palindrome(s)}")