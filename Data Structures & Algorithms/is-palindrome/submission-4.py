class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = ""
        for char in s:
            if char.isalnum():
                output += char.lower()

        return output == output[::-1]