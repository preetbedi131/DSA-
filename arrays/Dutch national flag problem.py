"""Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]"""

class Solution(object):
    def sortColors(self, nums):
        start,mid,end=0,0,len(nums)-1
        while mid<=end:
            if nums[mid]==0:
                nums[start],nums[mid]=nums[mid],nums[start]
                start+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:#if nums[mid]==2
                nums[mid],nums[end]=nums[end],nums[mid]
                end-=1


        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
