# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first

        return dummy.next
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def print_linked_list(head):
    while head:
        if head.next:
            print(str(head.val) + " →"),
        else:
            print(head.val)
        head = head.next
arr = [1, 2, 3, 4]
head = create_linked_list(arr)

print("Original List:")
print_linked_list(head)

sol = Solution()
swapped = sol.swapPairs(head)

print("\nSwapped Pairs List:")
print_linked_list(swapped)