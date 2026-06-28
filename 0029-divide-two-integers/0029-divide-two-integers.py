class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = abs(dividend) // abs(divisor)
        if (dividend < 0) != (divisor < 0):
            result = -result 
        if result > 2147483647:
            return 2147483647
            
        return result
        