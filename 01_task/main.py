from linked_list import LinkedList
from sort import insertion_sort
from merge import merge_ll


def main():
    print("Reverse demo:")
    reverse_linked_list_demo()
    print("-" * 50)
    print("Sort demo:")
    sorting_linked_list_demo()
    print("-" * 50)
    print("Merge demo:")
    merge_linked_list_demo()


def reverse_linked_list_demo():
    llist = LinkedList()

    llist.insert_at_end(15)
    llist.insert_at_end(10)
    llist.insert_at_end(5)
    print("Before reverse:")
    llist.print_list()  # 15, 10, 5
    llist.reverse()
    print("After reverse:")
    llist.print_list()  # 5, 10, 15


def sorting_linked_list_demo():
    llist = LinkedList()

    llist.insert_at_end(10)
    llist.insert_at_end(5)
    llist.insert_at_end(15)
    llist.insert_at_end(6)
    print("Before sorting:")
    llist.print_list()  # 10, 5, 15, 6
    insertion_sort(llist)
    print("After sorting:")
    llist.print_list()  # 5, 6, 10, 15


def merge_linked_list_demo():
    llist1 = LinkedList()
    llist1.insert_at_end(1)
    llist1.insert_at_end(4)
    llist1.insert_at_end(7)
    llist1.insert_at_end(10)

    llist2 = LinkedList()
    llist2.insert_at_end(2)
    llist2.insert_at_end(3)
    llist2.insert_at_end(8)

    result = merge_ll(llist1, llist2)
    result.print_list()


if __name__ == "__main__":
    main()
