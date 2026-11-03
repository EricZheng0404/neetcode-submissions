class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l, r = i, i
            mySet = set()
            mySet.add(s[l])
            while r + 1 < len(s) and s[r+1] not in mySet:
                r += 1
                mySet.add(s[r])
            res = max(res, len(mySet))
        return res