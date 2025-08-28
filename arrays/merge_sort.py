class Solution(object):
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums   
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid]) 
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)      

    def merge(self, left, right):
        s = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                s.append(left[i])
                i += 1
            else:
                s.append(right[j])
                j += 1

       
        s.extend(left[i:])
        s.extend(right[j:])  
        return s

    def sortArray(self, nums):
        return self.mergeSort(nums)
