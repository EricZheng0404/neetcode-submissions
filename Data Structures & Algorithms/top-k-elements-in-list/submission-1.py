class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict(int)
        for num in nums:
            mydict[num] += 1
            
        # sorted_by_value = sorted(mydict.items(), key=lambda item: item[1])
        # return sorted_by_value[:k-1]
        sorted_by_value = sorted(mydict.items(), key=lambda item: item[1], reverse=True)
        
        # Return only the keys of the top k elements
        return [item[0] for item in sorted_by_value[:k]]


            # mydict[num] = mydict[num, 0] + 1
        