from linked_list import LinkedList, Node


def insertion_sort(lst: LinkedList):
    head = lst.head
    if not head or not head.next:  # 0 or 1 elements in the list
        return lst

    head_placeholder = Node()  # serve as a first element
    current = head

    while current:
        next_tmp = current.next  # save the next element
        # find the last element which is smaller then current
        prev = head_placeholder
        while prev.next and prev.next.data < current.data:
            prev = prev.next
        # insert the current after prev
        current.next = prev.next
        prev.next = current
        current = next_tmp
    # replace the head of the list with the next element of the placeholder
    lst.head = head_placeholder.next
