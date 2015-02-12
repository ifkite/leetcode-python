class Solution:
    # @return a string
    def countAndSay(self, n):
        num = 1
        if n == 1:
            return str(n)
        for idx in range(n - 1):
            num = self.calc(num)
        return str(num)

    def calc(self,n):
        s=str(n)
        result = []
        loop = 1
        for idx in range(len(s)):
            if idx < len(s) - 1:
                if s[idx] == s[idx+1]:
                    loop += 1
                    idx += 1
                    if idx == len(s) - 1:
                        result.append(str(loop))
                        result.append(str(s[idx]))
                        break
                else:
                    result.append(str(loop))
                    result.append(str(s[idx]))
                    idx += 1
                    loop = 1
                    if idx == len(s) - 1:
                        result.append(str(1))
                        result.append(str(s[idx]))
                        break
            else:
                result.append(str(1))
                result.append(str(s[idx]))
                break
        return int("".join(result))
