class Solution:
    # @return an integer
    def reverse(self, x):
        li = list(str(x))
        if li[0].isdigit():
            li = [i for i in reversed(li)]
            res = ''.join(li)
            res.lstrip('0')
        else:
            li = [i for i in reversed(li)]
            li.pop()
            res = ''.join(li).lstrip('0')
            res = '-'+res
        if int(res) > 2147483647 or int(res) < -2147483647:
            return 0
        return int(res)