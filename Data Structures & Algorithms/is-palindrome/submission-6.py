class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        '''
        for char in s:
            if (char >= 'a' and char <= 'z'):
                string += char
            elif (char >= 'A' and char <= 'Z'):
                char = char.lower()
                string += char
            elif char >= '0' and char <= '9':
                string += char
        '''

        for char in s:
            if char.isalnum():
                string += char.lower()
                
        n = len(string)

        i = 0; j = n-1

        while i < (n//2):
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        
        return True
        