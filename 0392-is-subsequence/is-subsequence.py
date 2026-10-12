class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subp = 0
        strp = 0
        while subp < len(s) and strp < len(t):
            if s[subp] == t[strp]:
                subp += 1
            strp += 1
        if subp == len(s):
            return True
        return False