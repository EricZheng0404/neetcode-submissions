class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        myDict = dict()
        count1 = [0] * 26 # since there're only lowercase letters
        for char in s1:
            count1[ord(char) - ord('a')] += 1
        myDict[tuple(count1)] = 1 + myDict.get(tuple(count1), 0)

        l, r = 0, len(s1) 

        while r < len(s2) + 1:
            count2 = [0] * 26
            for char in s2[l:r]:
                count2[ord(char) - ord('a')] += 1
            if tuple(count2) in myDict:
                return True
            l += 1
            r += 1
        return False
                
        