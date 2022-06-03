#
class Solution:
    def isPalindrome(self, s: str) -> bool:    
        n = len(s)
        
        if n == 0:
            return True
        
        l = 0
        r = n-1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True