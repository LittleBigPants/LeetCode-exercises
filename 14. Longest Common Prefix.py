class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        prefix = ""
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != letter:
                    return prefix
            prefix += letter

        return prefix
            
