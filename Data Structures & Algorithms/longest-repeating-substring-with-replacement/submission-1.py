class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        myDict = defaultdict(int)
        length = len(s)

        for r in range(length):
            myDict[s[r]] += 1 # use the character at index r in s, not s[r] 
            while (r- l + 1 - max(myDict.values())) > k:
                myDict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res