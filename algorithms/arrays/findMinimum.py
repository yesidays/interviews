def find_minimum(arr):

    if len(arr) <= 0:
        return None

    minimum = arr[0]

    for number in arr:
        if number < minimum:

            minimum = number

    return minimum


def find_minimum_sort(arr):

    if len(arr) <= 0:
        return None

    arr.sort()
    return arr[0]


arr = [100, 12, 30, 3, 500, 1, 100]

print(find_minimum(arr))

print(find_minimum_sort(arr))