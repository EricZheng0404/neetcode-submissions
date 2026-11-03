class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = ""
        for char in s:
            if char.isalnum():
                output = output + char.lower()
        length = len(output)
        print(output)
        print("length", length)
        if length%2 == 0:
            for i in range(0, int(length/2)):
                if output[i] != output[length - 1 - i]:
                    return False
        else:
            for i in range(0, int(((length - 1) / 2))):
                print("i", i)
                print("output[i]:", output[i])
                print("output[length - 1 - i]:", output[length - 1 - i])
                if output[i] != output[length - 1 - i]:
                    return False
        return True