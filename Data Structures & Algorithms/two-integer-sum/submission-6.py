class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {} #val : index of the value
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict:
                return [my_dict[complement], i] 
                """
                The reason why it's not [i, my_dict[complement]] is 
                because we are checking the value:index in the dictionary
                so if there's a match, that means the value in the dictionary
                is a previous value, and nums[i] actually comes after that 
                value
                """
            my_dict[nums[i]] = i

'''
HashMap: 
Val : Index
We initialize an empty hashmap. The reason why we don't want to 
initialize the hashmap with all the values from the array is that 
the returned values of i and j can't be same indices. This means that
if the values are already in the hashmap, then if we're checking on 
the value 2, it's complment, 2, is actually also in the hash map. But 
i and j can't be the same value.
So, we need to:
1. Check the complement of a value is in the hashmap.
2. If so, we return the index of the value and the index of its 
complement. 
3. If not, we put the value and its index into the hashmap.

Time complexity: O(n) because we only need to iterate the array once.
Space complexity: O(n) because we need to store the hashmap (a 
dictionary)
'''