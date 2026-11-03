class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        total = 0
        
        for n in nums:
            total += n
            result = max(result, total)
            if total < 0:
                total = 0
        return result