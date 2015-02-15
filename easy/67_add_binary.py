class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        try:
            res = list(bin(int(a,2)+int(b,2)))
            if res[0] == '-':
                res.pop(1)
                res.pop(1)
                return "".join(res)
            else:
                res.pop(0)
                res.pop(0)
                return "".join(res)
        except ValueError:
            return '0'