
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            res = [[1], [1, 1]]
            for i in range(numRows - 2):
                seed = res[-1]
                last_row = [1]
                for idx in range(len(res)-1):
                    last_row.append(seed[idx]+seed[idx+1])
                last_row.append(1)
                res.append(last_row)
            return res

# if __name__ == '__main__':
#     solution = Solution()
#     print solution.generate(6)