"""Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2]."""


class Solution(object):
    def twoSum(self, numbers, target):
        i,j=0,len(numbers)-1
        while i<j:
           current_sum=numbers[i]+numbers[j]
           if current_sum==target:
               return [i+1,j+1]
           elif current_sum<target:
                i+=1
           else:
                j-=1
