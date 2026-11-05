class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Set up a defaultdict 
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        # turn into a tuple
        freq = freq.items()
        # Sort by the value
        # This gives a list of (key, value) tuples
        freq = sorted(freq, key=lambda x:x[1], reverse=True)
        # Get the first k
        res = []
        for k, v in freq[:k]:
            res.append(k)
        return res