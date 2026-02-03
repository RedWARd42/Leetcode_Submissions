class Solution:
    def bitwiseComplement(self, n: int) -> int:
        origin = str(bin(n))
        origin = origin[2:]
        res = ""
        for i in range(len(origin)):
            if origin[i] == "0":
                res += "1"
            if origin[i] == "1":
                res += "0"
        return int(res, 2)
