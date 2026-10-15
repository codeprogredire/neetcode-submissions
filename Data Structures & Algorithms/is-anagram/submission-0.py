class Solution:
    def freqCount(self,s):
        hm={}
        for char in s:
            if char in hm:
                hm[char]+=1
            else:
                hm[char]=1
        return hm

    def isAnagram(self, s: str, t: str) -> bool:        
        freq1=self.freqCount(s)
        freq2=self.freqCount(t)

        if freq1==freq2:
            return True
        else:
            return False