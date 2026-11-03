class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Construct two things, each record the frequencies of each character in two strings
        list_s, list_t = [0] * 26, [0] * 26
        for c1, c2 in zip(s, t):
            list_s[ord(c1) - ord('a')] += 1
            list_t[ord(c2) - ord('a')] += 1
        # To compare if the frequency of every character is the same
        print(list_s)
        print(list_t)
        for n1, n2 in zip(list_t, list_s):
            if n1 != n2:
                return False
        return True
        