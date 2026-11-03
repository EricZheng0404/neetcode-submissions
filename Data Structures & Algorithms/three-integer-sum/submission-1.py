class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length): # i, j, k must be distinct values. 
                for k in range(j + 1, length): # For example, [-2, 4, ...]. In this case, i could be 1, and j and k could be both 2.
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        result.add(tuple(temp))
        
        return [list(i) for i in result]
        