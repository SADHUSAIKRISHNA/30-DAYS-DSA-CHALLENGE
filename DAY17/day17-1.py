# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head
        
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail.next = head
        return new_head
def printList(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result))


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print("Original list:")
printList(n1)

sol = Solution()
rotated_head = sol.rotateRight(n1, 2)

print("Rotated by 2:")
printList(rotated_head)
