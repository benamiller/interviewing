from objects import SinglyLinkedList, print_singly_linked_list


def mergeLists(head1, head2):
    curr1 = head1
    curr2 = head2
    new_list = SinglyLinkedList()

    while curr1 is not None and curr2 is not None:
        if curr1.data < curr2.data:
            new_list.insert_node(curr1.data)
            curr1 = curr1.next
        else:
            new_list.insert_node(curr2.data)
            curr2 = curr2.next

    while curr1 is not None:
        new_list.insert_node(curr1.data)
        curr1 = curr1.next

    while curr2 is not None:
        new_list.insert_node(curr2.data)
        curr2 = curr2.next

    return new_list.head


if __name__ == "__main__":
    head1 = SinglyLinkedList()
    head1_values = list(map(int, input().strip().split()))

    for value in head1_values:
        head1.insert_node(value)

    head2 = SinglyLinkedList()
    head2_values = list(map(int, input().strip().split()))

    for value in head2_values:
        head2.insert_node(value)

    merged_list = mergeLists(head1.head, head2.head)
    print_singly_linked_list(merged_list, ' ')
