"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, 
we return the second one.
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # slow and fast is a node, not just a value
        # slow: moves one step at a time
        # fast: moves two steps at a time
        slow = fast = head

        while fast and fast.next: # fast is not None and fast.next is not None
            slow = slow.next
            fast = fast.next.next
        return slow  # This is the second middle node if length is even


# Example test
head = build_linked_list([1, 2, 3, 4, 5, 6])
sol = Solution()
middle = sol.middleNode(head)
print_linked_list(middle)  # Expected: 4 -> 5 -> 6 -> None
