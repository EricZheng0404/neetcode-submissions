class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # set is a reserved keyword
        for num in nums:
            if num in seen:
                return True
            seen.add(num) # it's set.add(), not array.append()
        return False

"""
set is better than list in this case because of the uniqueness of 
elements.
Also, lookup in set takes O(1) considering the underlying hashtable 
implementation, while it takes O(n) for list

Time complexity: O(n) because we need to go through every elements
in the array.
Space complexity: O(n) because the worst case scenario is that 
we need to put all the elements in the array into the set when 
there's no duplicate
"""