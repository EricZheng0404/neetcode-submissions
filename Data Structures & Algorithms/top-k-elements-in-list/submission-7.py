class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the freq of each number
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1 
        # Put them into the index-based freq table: buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():
            buckets[f].append(num)
        # Get the number from the back
        res = []
        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
        return res