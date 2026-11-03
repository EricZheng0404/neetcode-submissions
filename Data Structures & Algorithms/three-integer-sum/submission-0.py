class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)

        
        for i, a in enumerate(nums):
            if i != 0 and nums[i-1] == nums[i]: # the skip duplicate values for a
                continue
            l, r = i + 1, length - 1
            while l < r:
                numSum = a + nums[l] + nums[r]
                if numSum > 0:
                    r -= 1
                elif numSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                
            
        return result