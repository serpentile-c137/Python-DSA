def Permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
    
# Example usage
list1 = [1, 2, 3]
list2 = [3, 2, 1]
list3 = [1, 2, 4]
print(Permutation(list1, list2))  # Output: True
print(Permutation(list1, list3))  # Output: False

list4 = ['a', 'b', 'c']
list5 = ['c', 'b', 'a']
print(Permutation(list4, list5))  # Output: True