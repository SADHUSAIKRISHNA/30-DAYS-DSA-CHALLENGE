# Definition for a Node.
class Node(object):
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur, clone = head, head.next
        res = clone
        while cur:
            cur.next = cur.next.next
            clone.next = clone.next.next if clone.next else None
            cur = cur.next
            clone = clone.next

        return res
def print_list(head):
    while head:
        rand_val = head.random.val if head.random else "None"
        print("Node({}) → Random({})".format(head.val, rand_val))
        head = head.next
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3
node1.random = node3 
node2.random = node1  
node3.random = node2  

print("Original List:")
print_list(node1)

sol = Solution()
cloned_head = sol.copyRandomList(node1)

print("\nCloned List:")
print_list(cloned_head)