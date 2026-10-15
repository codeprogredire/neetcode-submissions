class Solution:
    def commonPrefix(self,s,t):
        common=""
        m=len(s)
        n=len(t)

        for i in range(min(m,n)):
            if s[i]==t[i]:
                common+=s[i]
            else:
                return common
        return common

    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=strs[0]

        for i in range(1,len(strs)):
            common=self.commonPrefix(common,strs[i])
            if common=="":
                return ""
        return common


        