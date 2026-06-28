class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        singleNum = int("".join(map(str, digits)))
        
        singleNum +=1
        finalResult = []
        for i in str(singleNum):
            finalResult.append(int(i))
        
        return finalResult
