# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        list_len = 0
        tmp = head
        while tmp:
            list_len += 1
            tmp = tmp.next
        if list_len == 0 or list_len == 1:
            return None
        del_num = list_len - n
        tmp = head
        if del_num == 0:
            tmp = head.next
            del head
            return tmp
        for i in range(del_num - 1):
            tmp = tmp.next
        tar = tmp.next
        tmp.next = tmp.next.next
        del tar
        return head
