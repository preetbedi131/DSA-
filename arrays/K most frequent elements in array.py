"""Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]"""



#Approach 1: Used most_common fn from Counter module
def topKFrequent(self, nums, k):
  d = Counter(nums)
  return [num for num,freq in d.most_common(k)]
  
#Approach 2:  Used bucket sort
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        d=Counter(nums)
        buckets=[[]for i in range(len(nums)+1)]  #used index as frequency
        for key,freq in d.items():
            buckets[freq].append(key)
        result = []
        for i in range(len(buckets),0,-1):
            for key in buckets[i]:
               result.append(key)
               if len(result)==k:
                  return result



        



        
