'''
    List of Products of All Elements
    Input: [1, 2, 3, 4]
    Output: [24, 12, 8, 6]
'''


def find_product(lst):
    
    a_of_products = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            if j != i:
                product = product * lst[j]
               
        a_of_products.insert(j, product)

    return a_of_products


def find_product_2(lst):
    result = []
    left = 1 
    for i in range(len(lst)):
        currentproduct = 1  
        for ele in lst[i+1:]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result
        

print(find_product([1, 2, 3, 4]))
print(find_product_2([1, 2, 3, 4]))