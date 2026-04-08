class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right = len(s) - 1
        s = s.lower()


        while left < right:
            while(not s[right].isalnum() and left < right):
                right -= 1
            while(not s[left].isalnum() and left < right):
                left += 1
            
            if(s[right] != s[left]):
                return False
            else:
                right -= 1
                left += 1
        
        return True
            

        