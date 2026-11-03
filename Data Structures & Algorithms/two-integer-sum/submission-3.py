class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            print("i: ", i)
            for j in range(i + 1, len(nums)):
                print("j: ", j)
                if nums[i] + nums[j] == target:
                    return [i, j]
    
"""
brute force method:
Use two iterations. The first iteration starts from the first element 
of the string and try to find its complement in the rest of list. 
If so, return a list of its index and its complement's index.
Time complexity: O(2n) because there're two iterations.
Space complexity: O(0) because there's no extra memory used.
"""