class Solution:
    def isPalindrome(self, x: int) -> bool:

        string = str(x)
        newString = "".join(reversed(string)) 
        if string == newString:
            return True
        else: 
            return False