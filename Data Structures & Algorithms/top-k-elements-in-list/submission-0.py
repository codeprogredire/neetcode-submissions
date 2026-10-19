class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = defaultdict(int)

        for num in nums:
            freqCount[num] += 1
        
        sorted_freq = dict(sorted(freqCount.items(),key=lambda item:item[1],reverse=True))

        ans = []
        for num in sorted_freq.keys():
            ans.append(num)

        return ans[:k]
        