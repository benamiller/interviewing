from objects import SinglyLinkedList


def compare_lists(llist1, llist2):
    curr_1 = llist1
    curr_2 = llist2

    while curr_1 is not None and curr_2 is not None:
        if curr_1.data != curr_2.data:
            return False

        curr_1 = curr_1.next
        curr_2 = curr_2.next

    return curr_1 is None and curr_2 is None


if __name__ == "__main__":
    llist1 = SinglyLinkedList()
    llist1_values = list(map(int, input().strip().split()))

    for value in llist1_values:
        llist1.insert_node(value)

    llist2 = SinglyLinkedList()
    llist2_values = list(map(int, input().strip().split()))

    for value in llist2_values:
        llist2.insert_node(value)

    print(compare_lists(llist1.head, llist2.head))
