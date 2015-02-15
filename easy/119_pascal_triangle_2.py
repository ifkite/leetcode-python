class Solution:
    # @return a list of integers
    # C(n,m)=n!/(m!(n-m)!)
    # n:row number, m:element number
    # from math import factorial
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        else:
            res = []
            for idx in range(rowIndex+1):
                res.append(self.calcEle(rowIndex,idx))
            return res

    def calcEle(self, n, m):
        dividend, divisor =1, 1
        for idx in range(1, n-m+1):
            dividend *= (idx + m)
            divisor *= idx
        return dividend // divisor

# if __name__ == '__main__':
#     solution = Solution()
#     print solution.getRow(4)