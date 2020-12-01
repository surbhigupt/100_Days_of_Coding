class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
		# Initializes ans and curSum to nums[0]
        ans, curSum = (nums[0],) * 2
        
        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            ans = max(ans, curSum)
        
        return ans