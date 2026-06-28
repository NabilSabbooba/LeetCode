class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #loop through the array
            #find the index the target first shows
            #save that index
            #check if the next number is the same. if it is save that index too
            #return the indices
        #if not found return [-1 ,-1]
        finalAnswer=[]
        for i in range(len(nums)):
            if nums[i] == target:
                finalAnswer.append(i)
        if finalAnswer == []:
            return [-1, -1]
        else:
            return [finalAnswer[0], finalAnswer[-1]]