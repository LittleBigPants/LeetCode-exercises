from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) -1
        i = 0
        while i<= k:
            if nums[i] == val:
                nums[i], nums[k] = nums[k], nums[i]
                nums.pop()
                k -= 1
            else:
                i += 1

        return len(nums)

# Example usage:
# sol = Solution()
# nums = [3, 2, 2, 3]
# val = 3
# result = sol.removeElement(nums, val)
# print(result)  # Output: 2
