class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = dict()
        for char in s1:
            map1[char] = 1 + map1.get(char, 0)

        l, r = 0, len(s1) 

        while r < len(s2) + 1:
            map2 = dict()
            print("substring: ", s2[l:r])
            for char in s2[l:r]:
                
                map2[char] = 1 + map2.get(char, 0)
            if map1 == map2:
                return True
            l += 1
            r += 1
        return False
                
        