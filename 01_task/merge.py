from linked_list import LinkedList, Node


def merge_ll(list1: LinkedList, list2: LinkedList) -> LinkedList:
    head_placeholder = Node()
    current = head_placeholder

    l1, l2 = list1.head, list2.head
    # until both lists have elements
    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            current = l1
            l1 = l1.next
        else:
            current.next = l2
            current = l2
            l2 = l2.next
    # l1 or l2 are already exhausted
    current.next = l1 if l1 else l2
    # replace the head of the list with the next element of the placeholder
    result = LinkedList()
    result.head = head_placeholder.next
    return result
