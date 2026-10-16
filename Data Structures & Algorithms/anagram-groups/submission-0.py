class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedList={}

        for s in strs:
            temp=list(s)
            temp.sort()
            temp=''.join(temp)
            
            if temp in sortedList:
                sortedList[temp].append(s)
            else:
                sortedList[temp]=[s]
        
        ans=list(sortedList.values())

        return ans



        