class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mydict = defaultdict(int)
        result = []
        for i in range(len(numbers)):
            if numbers[i] in mydict:
                result.append(mydict[numbers[i]])
                result.append(i + 1)
                return result
            mydict[target - numbers[i]] = i + 1