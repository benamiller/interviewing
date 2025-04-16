from objects import BinarySearchTree


def postOrder(root):
    if root is None:
        return

    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=" ")


if __name__ == "__main__":
    tree = BinarySearchTree()

    arr = list(map(int, input().split()))

    for item in arr:
        tree.create(item)

    postOrder(tree.root)
    print()
