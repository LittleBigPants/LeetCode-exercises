class Solution:
    def isZeroArray(self, nums, queries) -> bool:
        for q in queries:
            for n in range(len(nums)):
                if q[0]<=n<=q[1] and nums[n] != 0:
                    nums[n]-= 1
        if sum(nums) != 0:
            return False
        return True


class Solution(object):
    def isZeroArray(self, nums, queries):
        diff = [0] * (len(nums))
        for l, r in queries:
            diff[l] += 1
            if r + 1 < len(nums):
                diff[r + 1] -= 1
        cnt = 0
        for i in range(len(nums)):
            cnt += diff[i]
            if nums[i] > cnt:
                return False
        return True