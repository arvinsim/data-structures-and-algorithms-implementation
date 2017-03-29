from binary_tree import BinaryTree

def preorder(tree):
    """
    In a preorder traversal, we visit the root node first, then recursively do a preorder traversal 
    of the left subtree, followed by a recursive preorder traversal of the right subtree.
    """
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
    """
    In an inorder traversal, we recursively do an inorder traversal on the left subtree, visit the 
    root node, and finally do a recursive inorder traversal of the right subtree.
    """
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def postorder(tree):
    """
    In a postorder traversal, we recursively do a postorder traversal of the left subtree and the 
    right subtree followed by a visit to the root node.
    """
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


if __name__ == '__main__':
    r = BinaryTree('1')
    r.insertLeft('2')
    r.insertRight('3')
    r.getLeftChild().insertLeft('4')
    r.getLeftChild().insertRight('5')

    print('Preorder Traversal')
    preorder(r)

    print('Inorder Traversal')
    inorder(r)

    print('Postorder Traversal')
    postorder(r)
