class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]

        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j<k:
                total=nums[i]+nums[j]+nums[k]

                if total<0:
                    j+=1
                elif total>0:
                    k-=1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                    
        return result