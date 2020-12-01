class Solution:
    def climbStairs(self, n: int) -> int:
        
        step_dict = { 0:0, 1:1, 2:2}
        
        if n in step_dict:
            return step_dict[n]
        
        for i in range(3,n+1):
            step_dict[i] = step_dict[i-1] + step_dict[i-2]
        
        return step_dict[n]
        