def reverse_num(num):
    res = 0
    while num > 0:
        last = num % 10
        res = (res * 10) + last
        num //= 10
    
    return res


print(reverse_num(5873))