"""Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]"""

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
      n = len(nums)
      k = k % n 

      def reverse(left , right):
          while left < right:
              nums[left] , nums[right] = nums[right] , nums[left]
              left+=1 
              right-=1
      reverse(0, n-1)
      reverse(0, k-1)
      reverse(k, n-1)
