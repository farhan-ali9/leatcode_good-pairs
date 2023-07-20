class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=len(nums)
        count=0
        j=1
        for i in range(a):
          for j in range(a): 
              if nums[i]==nums[j] and i<j:
                  count+=1
        return count
