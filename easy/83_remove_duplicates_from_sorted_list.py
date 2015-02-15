# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return 'value of listnode is %d' %(self.val)

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        #length of list is 0
        if head == None:
            return None
        #length of list is 1
        elif head.next == None:
            return head
        #length of list is 2
        else:
            tmp = head
            next_nod = head.next
            while 1:
                if tmp.val == next_nod.val:
                    tmp.next = next_nod.next
                    next_nod = tmp.next
                else:
                    tmp = next_nod
                    next_nod = next_nod.next
                if next_nod == None:
                    break
            return head