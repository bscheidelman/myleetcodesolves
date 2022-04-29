class Solution(object):
    def longestCommonPrefix(self, strs):
        #Runtime: 18 ms
        #Memory: 13.7 MB
      
        rval = ""
        cval = ""
        lowest = 99999999999
        for val in strs:
            if len(val) < lowest:
                lowest = len(val)
        if len(strs) == 1:
            return strs[0]
        for num in range(lowest+1):
            check = 0
            cval = strs[0][0:num]
            for val in strs:
                if val[0:num] != cval:
                    check = 1
            if check == 1:
                break
            else:
                rval = cval
        return rval
        
