class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        prefix = 1
        for i in range(n):
            prefix *= nums[i]
            output.append(prefix)
        
        postfix = 1
        for i in range(n-1,-1,-1):
            if i == 0:
                output[i] = postfix * 1
            else:
                output[i] = postfix * output[i-1]
            postfix *= nums[i]
        
        return output

        
        