# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None: return head
        p,c,t=head,head.next,head.next.next
        p.next=None
        while t:
            c.next=p
            p=c
            c=t
            t=t.next
        c.next=p
        return c
