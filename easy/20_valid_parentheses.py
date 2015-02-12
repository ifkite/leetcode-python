class Solution:
    # @return a boolean
    def isValid(self, s):
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False
        else:
            stk = []
            sym_dict = {')':'(',']':'[','}':'{'}
            for sym in s:
                if sym in ('(','[','{'):
                    stk.append(sym)
                elif sym in [')',']','}']:
                    if len(stk) == 0:
                        return False
                    else:
                        if stk[-1] == sym_dict[sym]:
                            stk.pop()
                        else:
                            return False
                else:
                    return False
            return len(stk) == 0
