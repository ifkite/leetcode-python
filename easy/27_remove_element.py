class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A) == 0:
            return 0
        else:
            A.sort()
            remove_idx = []
            for idx in range(len(A)):
                if A[idx] == elem:
                    remove_idx.append(idx)
            for i, idx in enumerate(remove_idx):
                A.pop(idx-i)
            return len(A)
