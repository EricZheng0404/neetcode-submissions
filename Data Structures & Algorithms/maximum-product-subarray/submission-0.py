class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float('-inf') # this can't be 0, because there could be a singleton negative number as the input array
        for i in range(len(nums)):
            curr = 1
            for j in range(i, len(nums)):
                curr = curr * nums[j]
                result = max(result, curr)
        return result