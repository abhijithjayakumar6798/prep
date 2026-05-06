class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start=0
        max_len=0
        
        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l=l-1
                r=r+1
            return l+1,r-1
        
        for i in range(len(s)):
            l1,r1=expand(i,i)
            len1=r1-l1+1
            if len1>max_len:
                max_len=len1
                start=l1
            
            l2,r2=expand(i,i+1)
            len2=r2-l2+1
            if len2>max_len:
                max_len=len2
                start=l2
            
        return s[start:start+max_len]