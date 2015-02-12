class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        s = list(set(A))
        s.sort()
        for idx,e in enumerate(s):
            A[idx] = e
        return len(s)