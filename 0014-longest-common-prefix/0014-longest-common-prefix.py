class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])): # any other word could be choosen instead of the first (strs[0])
        
            char = strs[0][i] # char = each letter of the first word individually 

            for s in strs[1:]: # s will store all words except the first 
                if i >= len(s) or s[i] != char:
                    return prefix
            prefix += char

        return prefix