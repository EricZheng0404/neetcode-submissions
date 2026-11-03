class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict(int) # default value of int?
        # in the dictionary, it's num/no. of its occurences pair
        for num in nums:
            mydict[num] += 1
        
        # set up n + 1 empty lists
        mylist = [[] for _ in range(len(nums) + 1)] 

        for key, value in mydict.items():
            mylist[value].append(key)

        result = []
        for item in reversed(mylist):
            if len(item) != 0:
                result.extend(item)
        print(result)
        return result[:k]
            

        