# Binary tree

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



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)
tree.right.right. right = TreeNode(8)



print('Pre order')
print(tree.pre_order())

print('In order')
print(tree.in_order())

print('Post order')
print(tree.post_order())


