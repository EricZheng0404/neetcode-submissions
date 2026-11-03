class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT # it's "==" not "="

"""
To use hashmap: to use character as key and its count as value.
space complexity: O(n). Because we need extra memory for two dictionaries
time: O(n). We need to go through two string s and t
"""