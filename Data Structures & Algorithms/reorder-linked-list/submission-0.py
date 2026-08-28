# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slowPointer, fastPointer = head, head.next

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next 
            fastPointer = fastPointer.next.next 

        secondHalfPointer = slowPointer.next 
        previous = slowPointer.next = None

        while secondHalfPointer:
            temp = secondHalfPointer.next 
            secondHalfPointer.next = previous 
            previous = secondHalfPointer
            secondHalfPointer = temp 

        firstHalfPointer, secondHalfPointer = head,previous 

        while secondHalfPointer: 
            tmp1,tmp2 = firstHalfPointer.next,secondHalfPointer.next 
            firstHalfPointer.next = secondHalfPointer
            secondHalfPointer.next = tmp1 

            firstHalfPointer = tmp1 
            secondHalfPointer = tmp2 





        