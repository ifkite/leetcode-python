class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        res = []
        for ch in s:
            if ch.isdigit():
                res.append(ch)
            if ch.isalpha():
                res.append(ch.lower())
        flag = True
        for idx, val in enumerate(res):
            if idx >= len(res)/2:
                break
            if val != res[-(idx+1)]:
                flag = False
                break
        return flag