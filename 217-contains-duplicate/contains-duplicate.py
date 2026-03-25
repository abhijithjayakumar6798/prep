class Solution(object):
    def containsDuplicate(self, nums):
        A=set()
        for num in nums:
            if num in A:
                return True
            A.add(num)
        return False