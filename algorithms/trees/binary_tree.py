# Binary tree
from random import randint

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_node(self, value):
        if value == self.value:
            return 
        
        #Left side
        if value < self.value:
            if self.left:
                self.left.add_node(value)
            else:
                self.left = TreeNode(value)

        #Right side
        else:
            if self.right:
                self.right.add_node(value)
            else:
                self.right = TreeNode(value)

    
    def pre_order(self):
        """ 
            First it will visit the root then
            visit the left node and at last
            visit the right node and print
            a list in specific order

            Root -> Left -> Right 
        """
        nodes = [self.value]
        if self.left:
            nodes += self.left.pre_order()
        if self.right:
            nodes += self.right.pre_order()
        return nodes


    def in_order(self):
        """
            First i will visit the left node 
            then root and the last I will
            visit the right node and print
            a list in specific order

            Left -> Root -> Right
        """
        nodes = []
        if self.left:
            nodes += self.left.in_order()

        nodes.append(self.value)

        if self.right:
            nodes += self.right.in_order()

        return nodes

    def post_order(self):
        """
            First i will visit the left node 
            then right node and the last I will
            visit the root and print
            a list in specific order

            Left -> Right -> Root
        """
        nodes = []
        if self.left:
            nodes += self.left.post_order()
        if self.right:
            nodes += self.right.in_order()
        
        nodes.append(self.value)

        return nodes

    def search_max_value(self):
        if self.right is None:
            return self.value

        return self.right.search_max_value()

    def search_min_value(self):
        if self.left is None:
            return self.value
        
        return self.left.search_min_value()

    def sum_nodes_values(self):
        
        if self.left:
            left = self.left.sum_nodes_values()
        else:
            left = 0

        if self.right:
            right = self.right.sum_nodes_values()
        else:
            right = 0

        return left + right + self.value

    def count_nodes(self):
        right = 0
        left = 0
        if self.left:
            left = self.left.count_nodes()
        
        if self.right:
            right = self.right.count_nodes()

        return left + right + 1

    def find_node(self, value):
        
        if value == self.value:
            return True
        
        if value < self.value:
            if self.left:
                return self.left.find_node(value)

        if value > self.value:
            if self.right:
                return self.right.find_node(value)




"""
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)
tree.right.right. right = TreeNode(8)
"""

tree = TreeNode(5)

for i in range(1, 10):
    number = randint(1, 50)
    tree.add_node(number)


print('Pre order')
print(tree.pre_order())

print('In order')
print(tree.in_order())

print('Post order')
print(tree.post_order())

print(f'Max value is: {tree.search_max_value()}')
print(f'Min value is: {tree.search_min_value()}')

print(f'Sum of nodes values: {tree.sum_nodes_values()}')
print(f'Count nodes: {tree.count_nodes()}')

print(f'Find the number 23')
print(tree.find_node(23))


