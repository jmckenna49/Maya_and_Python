# Detailed Explanation of `dummy` and `tail` in the `mergeTwoLists` method:
# 
# The `dummy` node is a placeholder node. It doesn't contain any real data and is used only 
# to simplify the merging process. By having a dummy node at the start, we can easily return 
# the merged list by just returning `dummy.next`, which points to the first real node.
# 
# The `tail` pointer is the one that moves through the merged list. It starts at the `dummy` 
# node and is used to append nodes from either `l1` or `l2`. As we add nodes to the merged 
# list, `tail` is moved to point to the last node added.
# 
# Here’s the breakdown:
#
# 1. **Initialization:**
#    - `dummy = ListNode()` creates an empty placeholder node.
#    - `tail = dummy` makes `tail` point to the `dummy` node. `tail` will be used to track 
#      where to add the next node in the merged list.
# 
# 2. **While Loop:**
#    - The loop `while l1 and l2:` compares nodes from both lists `l1` and `l2`. 
#    - If the value of `l1`'s node is smaller, we attach it to `tail.next` and move `l1` to 
#      the next node. Otherwise, we attach `l2` to `tail.next` and move `l2` to the next node.
#    - After appending a node, we move `tail` to `tail.next`, so `tail` always points to the 
#      last node in the merged list.
# 
# 3. **Remaining Nodes:**
#    - After the loop, one of the lists may still have remaining nodes. We append the rest of 
#      the nodes from either `l1` or `l2` to the merged list.
#    - This ensures that any remaining nodes are attached after all comparisons have been made.
# 
# 4. **Returning the Merged List:**
#    - After the while loop and the remaining node handling, the `dummy` node's `next` pointer 
#      will be pointing to the first real node in the merged list.
#    - We return `dummy.next`, effectively skipping the `dummy` node and returning the 
#      merged linked list starting from the first real node.
# 
# Example:
# 
# l1: 1 -> 3 -> 5
# l2: 2 -> 4 -> 6
#
# Result after merging:
# dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
#
# We return `dummy.next`, which points to the first real node in the merged list (`1`).



# DETAILED EXAMPLE OF DUMMY AND TAIL:
# Step-by-Step Walkthrough:
# Initial Setup:

# dummy is created: dummy -> null
# tail points to dummy: tail -> dummy -> null
# First Iteration (Compare l1.value = 1 and l2.value = 2):

# Since 1 < 2, we set tail.next to l1:
# tail.next = l1  # tail.next -> 1 (from l1)
# l1 = l1.next    # Move l1 to the next node: l1 -> 3 -> 5

# Now, tail moves to tail.next (the node we just added):
# tail = tail.next  # tail -> 1

# List so far:
# dummy -> 1 -> null
# tail points to 1.


# Second Iteration (Compare l1.value = 3 and l2.value = 2):

# Since 2 < 3, we set tail.next to l2:
# tail.next = l2  # tail.next -> 2 (from l2)
# l2 = l2.next    # Move l2 to the next node: l2 -> 4 -> 6
# Now, tail moves to tail.next (the node we just added):
# tail = tail.next  # tail -> 2
# List so far:

# dummy -> 1 -> 2 -> null
# tail points to 2.
# Third Iteration (Compare l1.value = 3 and l2.value = 4):

# Since 3 < 4, we set tail.next to l1:
# tail.next = l1  # tail.next -> 3 (from l1)
# l1 = l1.next    # Move l1 to the next node: l1 -> 5
# Now, tail moves to tail.next (the node we just added):
# tail = tail.next  # tail -> 3
# List so far:

# dummy -> 1 -> 2 -> 3 -> null
# tail points to 3.
# Continue Iterations:

# The process continues in the same way, with tail.next being updated to the next node in l1 or l2, and then tail moving forward.
# Final Merged List:

# After all iterations, we’ll have a merged list:
# dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Finally, we return dummy.next, which points to the first real node in the merged list (node with value 1).


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode() #creates an empty list
    tail = dummy # pointer to the same empty node now, so when we return dummy we're returning the head since dummy is a place holder that doesn't change
    
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    # this is in case one of the linked lists is null, the other list will add onto it as a remainder
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    
    return dummy.next

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
    head2 = ListNode(1, ListNode(1, ListNode(4, ListNode(5))))
    
    print("Original linked list:")
    print_linked_list(head)

    print("Original linked list2:")
    print_linked_list(head2)

    merged_linked_list = mergeTwoLists(head, head2)

    print("Reversed linked list:")
    print_linked_list(merged_linked_list)