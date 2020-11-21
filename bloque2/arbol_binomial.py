class Tree:
 
    def __init__(self, value=None, left=None, right=None):
 
        self.left = left
        self.right = right
        self.value = value
 
    def PrintTree(self):
        print(self.value)

arbol=Tree(20)
arbol.PrintTree()

# 1st method
root = Tree(8, Tree(3), Tree(10))
root.PrintTree()
 
# 2nd method
root = Tree(8)
root.left = Tree(3)
root.right = Tree(10)
root.PrintTree()

print("~"*40)

class Tree:
 
    def __init__(self, value, left=None, right=None):
 
        self.left = left
        self.right = right
        self.value = value
 
    def PrintTree(self):
        print(self.value)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
 
 
root = Tree(8)
root.left = Tree(3)
root.right = Tree(10)
root.left.left = Tree(1)
root.left.right = Tree(6)
root.right.right = Tree(14)
 
root.PrintTree()