class Solution(object):
    def searchInsert(self, nums, target):
        #Runtime: 38 ms
        #Memory: 14.1 MB
      
        if nums.count(target) > 0:
            return nums.index(target)
        if nums[0] > target:
            return 0
        sindex = 0
        while nums[sindex] < target:
            sindex += 1
            if sindex == len(nums):
                break
        return sindex
