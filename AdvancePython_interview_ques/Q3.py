# Explain Mutable Default Arguments Trap

def append_item(item, my_list=[]):
    my_list.append(item)
    return my_list

arr1 = append_item(1)  # [1]
arr1.append_item(2)  # [1, 2] ← Unexpected!
print(arr1)  # Output: [1, 2]

# To Fix: Use None and create inside function:


def append_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

append_item(1)  # [1]
append_item(2)  # [1, 2] ← Unexpected!