class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 0
        for n in range(1,len(nums),1):
            if nums[k] != nums[n]:
                k += 1
                nums[k] = nums[n]
        return k+1
        

test=[1,1,2]
solution = Solution()
print(solution.removeDuplicates(test))