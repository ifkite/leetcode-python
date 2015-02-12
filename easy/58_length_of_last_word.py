class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.lstrip()
        if len(s) == 0:
            return 0;
        li = s.split()
        return len(li[-1])
