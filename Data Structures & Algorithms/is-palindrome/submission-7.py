class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr  = "".join(c.lower() for c in s if c.isalnum())
        new_str = newstr[::-1]
        
        if newstr == new_str:
            return True
        else:
            return False