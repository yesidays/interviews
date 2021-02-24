'''
    Write a function that takes in a non-empty array of distinct integers representing
    a target sum.

    Difficulty: Easy

    Input:
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        targetSum = 10

    Output:
        [-1, 11]
    
'''

#O(n^2) - traverse
def twoNumberSum(array, targetSum):
	for i in range(len(array) - 1):
		firstNum = array[i]
		for j in range(i + 1, len(array)):
			secondNumber = array[j]
			if firstNum + secondNumber == targetSum:
				return [firstNum, secondNumber]
	return []


def twoNumberSum_2(array, targetSum):
	nums = {}
	for number in array:
		match = targetSum - number
		if match in nums:
			return [match, number]
		else:
			nums[number] = True
	return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

print(twoNumberSum(array, targetSum))
print(twoNumberSum_2(array, targetSum))