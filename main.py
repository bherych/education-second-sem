from node import BinaryTree

def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:

    found_target = [False]
    result = [None]

    def inorder(current: BinaryTree):
        if not current or result[0]:
            return
        
        inorder(current.left)

        if found_target[0] and current.value > node.value:
            if result[0] is None:
                result[0] = current
            return
        
        if current == node:
            found_target[0] = True

        inorder(current.right)

    inorder(tree)
    return result[0]


def main():

    root = BinaryTree(10)
    node5 = BinaryTree(5, parent=root)
    node15 = BinaryTree(15, parent=root)
    node3 = BinaryTree(3, parent=node5)
    node7 = BinaryTree(7, parent=node5)
    node20 = BinaryTree(20, parent=node15)
    node12 = BinaryTree(12, parent=node20)

    root.left = node5
    root.right = node15
    node5.left = node3
    node5.right = node7
    node20.left = node12
    node15.right = node20

    res = find_successor(root, node3)
    print(res.value)

main()