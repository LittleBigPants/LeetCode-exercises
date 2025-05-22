class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        k = 0
        start = 0

        if needle in haystack:
            while i < len(haystack):
                if haystack[i] == needle[k]:
                    if k == 0:
                        start = i 
                    k += 1
                    if k == len(needle):
                        return start
                    i += 1
                else:
                    if k > 0:
                        i = start + 1  
                    else:
                        i += 1
                    k = 0
        return -1
# Example usage:
solution = Solution()
haystack = "hello"
needle = "ll"
result = solution.strStr(haystack, needle)
print(result)  # Output: 2