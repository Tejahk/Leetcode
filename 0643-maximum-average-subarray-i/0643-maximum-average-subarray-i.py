class Solution(object):
    def findMaxAverage(self, nums, k):
        sum=0
        maxi=float('-inf')
        for r in range(len(nums)):
            sum+=nums[r]
            if r>=k-1:
                maxi=max(maxi,sum)
                sum-=nums[r-k+1]
        return float(maxi)/k
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        