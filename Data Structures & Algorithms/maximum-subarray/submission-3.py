class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')

        for start in range(len(nums)):
            currSum = nums[start]
            maxSum = max(maxSum, currSum)
            print("currSum: ", currSum)
            for end in range(start, len(nums)):
                if end <= start:
                    continue
                else: 
                    print("nums[end]", nums[end])
                    currSum += nums[end]
                    maxSum = max(currSum, maxSum)

        return maxSum