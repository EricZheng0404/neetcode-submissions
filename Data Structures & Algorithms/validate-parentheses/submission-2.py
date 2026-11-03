class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {')': '(', '}': '{', ']': '['}
        myStack = []

        for c in s:
            if c not in myDict:
                myStack.append(c)
                continue
            if not myStack or myStack[-1] != myDict[c]:
                return False
            else: 
                myStack.pop()
        return len(myStack) == 0