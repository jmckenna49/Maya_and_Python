# first iteration
# 1 -> 2 -> 3 -> 4 -> None
# current is 1, next node is 2, we reverse the pointer so curr.next = prev or 1->None
# prev to 1 and current to 2

# second iteration
# 1 <- 2 -> 3 -> 4 -> None
#   prev  current
# current is 2, next node is 3, we reverse the pointer so curr.next = prev or 2->1
# prev to 2 and current to 3 etc

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Temporarily store the next node, if 1->2->3->4->None, and we're on 1, next_node saves 2
        current.next = prev       # Reverse the current node's pointer, 1->None, breaks link to 2
        prev = current            # Move `prev` to the current node, last none in the reversed list
        current = next_node       # Move to the next node in the list, this now points at 2

    return prev  # `prev` becomes the new head of the reversed list

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    print("Original linked list:")
    print_linked_list(head)

    reversed_head = reverse_linked_list(head)

    print("Reversed linked list:")
    print_linked_list(reversed_head)
