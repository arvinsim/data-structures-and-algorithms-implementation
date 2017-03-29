class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.data:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.data:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)

if __name__ == '__main__':
    bst = Node(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(8)

    print(bst.contains(8))
    print(bst.contains(15))
    print(bst.contains(99999))
