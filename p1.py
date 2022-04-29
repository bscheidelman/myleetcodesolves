class Solution(object):
    def twoSum(self, nums, target):
        #Runtime: 8376 ms
        #Memory: 14.4 MB
        
        for num in range(len(nums)):
            for onum in range(len(nums)):
                if num != onum:
                    if (nums[num] + nums[onum]) == target:
                        return([num, onum])
