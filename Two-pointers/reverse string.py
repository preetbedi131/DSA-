"""Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Using Two pointers"""

class Solution(object):
    def reverseString(self, s):
       j = len(s) - 1
       for i in range(len(s) // 2):
            s[i], s[j] = s[j], s[i]
            j -= 1
