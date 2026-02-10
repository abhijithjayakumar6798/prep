class Solution(object):
    def containsDuplicate(self, nums):
        A=set()
        for num in nums:
            if num not in A:
                A.add(num)
            else:
                return True
        return False
