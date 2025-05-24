class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestResult = ''
        def palindromSearch(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]
        for i in range(len(s)):
            oddPalindrome = palindromSearch(i, i)
            evenPalindrome = palindromSearch(i, i + 1)

            if len(oddPalindrome) > len(evenPalindrome):
                longerPalindrome = oddPalindrome
            else:
                longerPalindrome = evenPalindrome

            if len(longerPalindrome) > len(bestResult):
                bestResult =longerPalindrome

        return bestResult
# Example usage:
solution = Solution()
s = "babad"
result = solution.longestPalindrome(s)
print(result)  # Output: "bab" or "aba"
# The longest palindromic substring in "babad" is either "bab" or "aba".
# Both are valid outputs.
# You can test with other strings as well.