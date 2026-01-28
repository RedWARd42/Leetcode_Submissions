class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        setone = {}
        settwo = {}

        for i in range(len(s)):
            if not s[i] in setone:
                setone[s[i]] = 1
            else:
                setone[s[i]] += 1

            if not t[i] in settwo:
                settwo[t[i]] = 1
            else:
                settwo[t[i]] += 1

        if setone != settwo:
            return False
        
        return True


        