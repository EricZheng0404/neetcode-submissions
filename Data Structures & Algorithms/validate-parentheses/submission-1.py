class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {')': '(', '}': '{', ']': '['}
        myStack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                myStack.append(char)
            if char == ')' or char == '}' or char == ']':
                if len(myStack) == 0:
                    return False
                if myDict[char] != myStack[-1]:
                    return False
                else:
                    myStack.pop()
        return len(myStack) == 0