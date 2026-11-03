class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        supplement = {}
        for i, num in enumerate(nums):
            if num in supplement:
                return [supplement[num], i]
            supplement[target - num] = i