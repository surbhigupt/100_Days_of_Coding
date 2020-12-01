class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def factorial(x):
            r = 1
            while x > 1:
                r *= (x)
                x -= 1
            return r
        
        return int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))
        