class Solution(object):
    def twoSum(self, nums, target):
        for i,val in enumerate(nums):
            for j in range(i+1,len(nums)):
                if nums[j]==(target-val):
                    return [i,j]

        