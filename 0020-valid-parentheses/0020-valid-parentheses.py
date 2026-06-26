class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else: 
                if not stack:
                    return False
                
                lastOpenBracket = stack.pop() #last char in stack
                neededOpenBracket = pairs[i]
                
                if lastOpenBracket != neededOpenBracket:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False        

                