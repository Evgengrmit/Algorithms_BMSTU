from reverse_linked_list import *


def find_cycle(this_list=LinkedList()):
    slow = this_list.head_node
    fast = this_list.head_node.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next
        else:
            return False
        if fast is None:
            return False
        if fast == slow:
            return True
    return False

