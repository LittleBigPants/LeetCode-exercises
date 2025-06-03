class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

# Example usage:
# solution = Solution()
# a = "1010"
# b = "1101"
# result = solution.addBinary(a, b)
# print(result)  # Output: "10111"
