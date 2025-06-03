class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# Example usage:
# solution = Solution()
# n = 5
# result = solution.climbStairs(n)
# print(result)  # Output: 8
# Note: This is a recursive solution and may not be efficient for large n due to exponential time complexity.