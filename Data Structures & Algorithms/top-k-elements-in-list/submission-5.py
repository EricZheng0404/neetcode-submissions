class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the numbers using defaultdict: num: freq
        freq = Counter(nums)
        # Fill the freq list, when index meaning freq
        index = [[] for _ in range(len(nums) + 1)]
        for n, f in freq.items():
            index[f].append(n)
        # Collecting numbers from backwards
        res = []
        for lst in index[::-1]:
            for num in lst:
                res.append(num)
                if len(res) == k:
                    return res
        return res
                