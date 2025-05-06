class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        for e in range(len(nums)):
            for x in range(len(nums)+1):
                 if(nums[e]+nums[x] == target):
                    print("paso")
                    return [e,x]
