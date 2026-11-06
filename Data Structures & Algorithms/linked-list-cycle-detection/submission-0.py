# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        Rabbit = head
        Turtle = head

        while Rabbit is not None and Rabbit.next is not None:
            Turtle = Turtle.next
            Rabbit = Rabbit.next.next

            if Turtle == Rabbit:
                return True
        
        return False

        