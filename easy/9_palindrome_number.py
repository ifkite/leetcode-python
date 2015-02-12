class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        res,reminder = divmod(x,10)
        if res == 0:
            return True
        if reminder == 0:
            return False

        x_len = 0
        res = x
        while True:
            res,reminder = divmod(res,10)
            x_len += 1
            if res == 0:
                break
        res = x
        rev = 0
        print 'x_len:%d' %(x_len)
        for i in range(x_len/2):
            res,reminder = divmod(res,10)
            rev = rev * 10 + reminder
        if x_len%2 !=0:
            res,tmp = divmod(res,10)
        return rev==res
