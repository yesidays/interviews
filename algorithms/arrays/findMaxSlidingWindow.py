"""
    Given an array of integers, find the maximum value in a window.

    input: array[-4, 2, -5, 3, 6]
    window_size = 3

    First window: max = 2, [-4, 2, 5]
    Second window: max = 3, [2, -5, 3]
    Thrid window: max = 6, [-5, 3, 6]

"""

#O(n)
def find_max_slinding_window(arr, window_size):
    result = []
    count = 0
    mov_window_size = 1
    while mov_window_size < len(arr):
        
        mov_window_size = window_size + count
        values = arr[count: mov_window_size]
        values.sort()

        max_value = values[window_size - 1]
        result.append(max_value)
        count += 1
    
    return result
        

        
    
    



arr = [-4, 2, -5, 3, 6]
window_size = 3
print(find_max_slinding_window(arr, window_size))