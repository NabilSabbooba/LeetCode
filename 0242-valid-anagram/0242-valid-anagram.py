class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        wordOne = "".join(sorted(s))
        wordTwo = "".join(sorted(t))
        if wordOne == wordTwo: return True
        else: return False