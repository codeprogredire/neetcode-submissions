class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        
        triplets = set()
        ans = []

        for i in range(n):
            j = i+1
            k = n-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    triplet = (nums[i],nums[j],nums[k])
                    if triplet not in triplets:
                        triplets.add(triplet)
                        ans.append(list(triplet))
                    j +=1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
        
        return ans