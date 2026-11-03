class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Go through each word, use their alphabet list as the key. Add them to a dictionary
        mapping = defaultdict(list)
        for s in strs:
            lst = [0] * 26
            for c in s:
                lst[ord(c) - ord('a')] += 1
            mapping[tuple(lst)].append(s)
        # Return the dictionary as a list
        res = []
        for _, v in mapping.items():
            res.append(v)
        return res