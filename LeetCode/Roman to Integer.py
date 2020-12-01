class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
               'D': 500, 'M': 1000}
        res = 0
        decimal = float('-inf')
        for i in s[::-1]:
            decimal = max(decimal, dic[i])
            if dic[i] < decimal:
                res -= dic[i]
            else:
                res += dic[i]
        return res