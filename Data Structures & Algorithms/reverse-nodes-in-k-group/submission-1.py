# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        g=0
        while cur and g < k:
            cur = cur.next
            g += 1
        
        if g == k:
            cur= self.reverseKGroup(cur, k)
            while g > 0:
                temp = head.next
                head.next = cur
                cur = head
                head = temp
                g -= 1
            head = cur
        return head