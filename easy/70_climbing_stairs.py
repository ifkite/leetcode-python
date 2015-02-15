class Solution:
    # @param n, an integer
    # @return an integer
    # f(n) = f(n-1) + f(n-2)
    # f(1) = 1
    # f(2) = 2
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            start_a = 1
            start_b = 2
            idx = 3
            while idx <= n:
                res = start_b + start_a
                start_a = start_b
                start_b = res
                idx += 1
            return res

if __name__ == '__main__':
    solution = Solution()
    print solution.climbStairs(4)