def armstrong_num(num):
    n = num
    res = 0
    while n > 0:
        last = n % 10
        res = res + (last ** len(str(num)))
        n //= 10
    return res == num

print(armstrong_num(153))  # True
print(armstrong_num(123))  # False