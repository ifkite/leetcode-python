# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# {1,3,5,7,9,11,13,15,17,19,21}, {2}
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        else:
            lenA, lenB = 0, 0
            iterA, iterB = headA, headB
            while iterA is not None:
                iterA = iterA.next
                lenA += 1
            while iterB is not None:
                iterB = iterB.next
                lenB += 1
            iterA, iterB = headA, headB
            if lenA < lenB:
                iterB = headB
                for idx in range(lenB-lenA):
                    iterB = iterB.next
            else:#lenA >= lenB
                iterA = headA
                for idx in range(lenA-lenB):
                    iterA = iterA.next

            while (iterA != iterB):
                iterA = iterA.next
                iterB = iterB.next
                if iterA is None or iterB is None:
                    return None
            return iterA

# author: backofhan
# https://oj.leetcode.com/discuss/22125/share-my-python-code
# class Solution:
#     # @param two ListNodes
#     # @return the intersected ListNode
#     def getIntersectionNode(self, headA, headB):
#         pA, pB = headA, headB
#         idx = 0
#         while pA != pB:
#             print idx
#             idx += 1
#             try:
#                 pA = pA.next
#                 print 'pA val: %d' %(pA.val)
#             except:
#                 pA = headB
#
#             try:
#                 pB = pB.next
#                 print 'pB val: %d'%(pB.val)
#             except:
#                 pB = headA
#         return pA
#
# if __name__ == '__main__':
#     solution = Solution()
#     head1 = ListNode(1)
#     n1 = ListNode(3)
#     n2 = ListNode(5)
#     n3 = ListNode(7)
#     n4 = ListNode(9)
#     head1.next = n1
#     n1.next = n2
#     n2.next = n3
#     n3.next = n4
#     head2 = ListNode(2)
#     b2 = ListNode(20)
#     head2.next = b2
#     b2.next = n3
#     # b2.next = n4
#     print solution.getIntersectionNode(head1,head2).val