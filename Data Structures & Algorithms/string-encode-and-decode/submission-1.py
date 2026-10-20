class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            n=len(s)
            token=str(n)+'#'
            encoded_string += (token + s)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        i=0
        while i < len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            decoded_list.append(s[j+1:j+1+length])
            i=j+length+1
        return decoded_list

