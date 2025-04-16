from objects import BinarySearchTree


def preOrder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)


if __name__ == "__main__":
    tree = BinarySearchTree()

    arr = list(map(int, input().split()))

    for i in range(len(arr)):
        tree.create(arr[i])

    preOrder(tree.root)
    print()
