def extract_digits(n):
    while n > 0:
        last = n % 10
        print(last)
        n = n // 10

extract_digits(5873)