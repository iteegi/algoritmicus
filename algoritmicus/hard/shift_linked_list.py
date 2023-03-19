"""Shift Linked List algorithm."""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shift_linked_list(head: LinkedList, k: int) -> LinkedList:
    """Shifts the list in place by k positions, and returns its new head.

    O(N) time | O(1) space

    :param head: The LinkedList in which to move the elements.
    :type head: LinkedList
    :param k: The number of positions to shift elements in the LinkedList.
    :type k: int
    :return: LinkedList moved items in the pot.
    The list is the same as the original one.
    :rtype: LinkedList
    """
    list_length = 0
    list_tail = head

    while list_tail:
        list_length += 1
        next_elm = list_tail.next
        if not next_elm:
            break
        list_tail = next_elm

    offset = abs(k) % list_length
    if offset == 0:
        return head

    new_tail_position = list_length - offset if k > 0 else offset
    new_tail = head

    for i in range(1, new_tail_position):
        new_tail = new_tail.next

    new_head = new_tail.next
    list_tail.next = head
    new_tail.next = None

    return new_head


def linked_list_to_array(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array


if __name__ == '__main__':
    head = LinkedList(0)
    head.next = LinkedList(1)
    head.next.next = LinkedList(2)
    head.next.next.next = LinkedList(3)
    head.next.next.next.next = LinkedList(4)
    head.next.next.next.next.next = LinkedList(5)
    array = linked_list_to_array(head)
    print(array)
    result = shift_linked_list(head, 2)
    array = linked_list_to_array(result)

    print(array)
