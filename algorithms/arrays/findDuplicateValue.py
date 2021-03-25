"""
    Given an array of integers between 1 and n, inclusive, where n is the lenght of the
    array.

    if no integer appears more than once, your function should be return -1

    array = [2, 1, 5, 2, 3, 3, 4]
    output: 2

"""
def firstDuplicateValue(array):
    found_numbers = {}
    for i in range(len(array)):
        number = array[i]
        resp = -1
        if array[i] in found_numbers:
            count = found_numbers.get(number)
            found_numbers[number] = count + 1
            if found_numbers.get(number) == 2:
                resp = number
                break
        else:
            found_numbers[number] = 1

    return resp



arr = [2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(arr))