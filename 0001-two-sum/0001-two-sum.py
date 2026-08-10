class Solution(object):
    def twoSum(self, nums, target):
        l=[]
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                sum= nums[i]+nums[j]
                if sum==target:
                   l.append(i)
                   l.append(j)
                   return l
                else:
                    continue
                 
        