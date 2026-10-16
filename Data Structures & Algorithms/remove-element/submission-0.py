class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=nums.count(val)
        n=len(nums)
        for i in range(n):
            if nums[i]==val:
                nums[i]=51
        
        nums.sort()

        return n-count

        