class Solution(object):
    def runningSum(self, nums):
        running_sum = 0
        ans = []
        for i in range (0,len(nums)):
            running_sum+=nums[i]
            ans.append(running_sum)
        return ans  
            
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        