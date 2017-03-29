class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def insertLeft(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t

    def insertRight(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key


if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())