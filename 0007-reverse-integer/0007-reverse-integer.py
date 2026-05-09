class Solution:
    def reverse(self, x: int) -> int:

        if x < 0: 
            reversedX = "".join(reversed(str(abs(x))))
            answer = int(reversedX) * -1
        else:
            reversedX = "".join(reversed(str(x)))
            answer = int(reversedX)
    
        if answer <  -2**31 or answer > 2**31 -1:
            return 0
        else:
            return answer