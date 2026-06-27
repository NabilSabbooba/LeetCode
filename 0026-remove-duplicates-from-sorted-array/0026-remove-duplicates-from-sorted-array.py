class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        i =0
        while i < len(nums) -1 - k:
            if nums[i] == nums[i+1]:
                nums.append(nums[i])
                nums.pop(i)
                k +=1
            
            else:
                i +=1
        k = len(nums) -k
        return k