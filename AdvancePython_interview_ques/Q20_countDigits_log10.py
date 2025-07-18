from math import *

def count_digits(num):
    return int(log10(num)+1) if num > 0 else 1
    

print(count_digits(5873))