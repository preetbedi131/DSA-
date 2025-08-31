"""Given a string s, return true if the s can be palindrome after deleting at most one character from it
Example 1:

Input: s = "aba"
Output: true"""

class Solution(object):
    def validPalindrome(self, s):
        def ispalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return ispalindrome(left+1,right)or ispalindrome(left,right-1)
            left+=1
            right-=1
        return True

            
        
