class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i,val in enumerate(nums):
            d=target-val
            if d in seen:
                return seen[d],i
            seen[val]=i