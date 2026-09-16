class Solution(object):
    def twoSum(self, nums, target):
        s ={}
        for i,num in enumerate(nums):
            c=target -num
            if c in s:
                return [s[c],i]
            s[num]=i

    
        