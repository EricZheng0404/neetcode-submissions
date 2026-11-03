class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        postfix = [0] * length

        result_front = 1
        result_back = 1

        for i in range(length):
            result_front = result_front * nums[i]
            result_back = result_back * nums[length - 1 - i]
            prefix[i] = result_front
            postfix[length - 1 - i] = result_back
        

        final_result = [0] * length
        final_result[0] = postfix[1]
        final_result[-1] = prefix[-2]
        for i in range(1, length - 1):
            final_result[i] = prefix[i - 1] * postfix[i + 1]
        return final_result

