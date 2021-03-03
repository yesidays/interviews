'''
    Given two non-empty arrays of integers, write a function that determines
    whether the second array is a subsequence of the first one.

    A subsequence of an array is a set of numbers aren't neccesarily adjacent
    in the array but that are in the same order as they appear in the array.

    Ej. [1, 3, 4] is a subsequence of [1, 2, 3, 4] and do so [2, 4]

    Return True or False
'''


# O(n)
def isValidSubsequence(array, sequence):
    arrId = 0
    seqId = 0
    if len(sequence) > len(array):
        return False

    while arrId < len(array) and seqId < len(sequence):
        if array[arrId] == sequence[seqId]:
            print(array[arrId], sequence[seqId])
            seqId += 1
        arrId += 1

    if seqId == len(sequence):
        return True

    return False



array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 22, 25, 6, -1, 8, 10]
print(isValidSubsequence(array, sequence))


array = [1, 1, 1, 1, 1]
sequence = [1, 1, 1]
print(isValidSubsequence(array, sequence))
