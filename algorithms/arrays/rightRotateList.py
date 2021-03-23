'''
    Implement a function right_rotate(lst, k) which will rotate the given list by k. 
    This means that the right-most elements will appear at the left-most position in the list and so on. 
    You only have to rotate the list by one element at a time.
    
    Input
    lst = [10, 20, 30, 40, 50]
    n = 3

    Output
    lst = [30, 40, 50, 10, 20]

'''

def right_rotate(lst, k):
    total = len(lst)
    right = lst[:total-k]
    left = lst[total - k:]
    
    return left + right

def right_rotate_k(lst, k):
    k = 0 if len(lst) == 0 else k % len(lst)
    return lst[-k:] + lst[:-k]



arr = [300, -1, 3, 0]
k = 3

print(right_rotate(arr, k))
print(right_rotate_k(arr, k))