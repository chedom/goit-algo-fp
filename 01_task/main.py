from linked_list import LinkedList


def main():
    reverse_linked_list()


def reverse_linked_list():
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    llist.print_list()
    llist.reverse()
    llist.print_list()


if __name__ == "__main__":
    main()
