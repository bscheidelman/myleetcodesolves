class Solution(object):
    def isPalindrome(self, x):
        #Runtime: 142 ms
        #Memory: 13.3 MB
        
        temp = str(x)
        eli = []
        for val in temp:
            eli.append(val)

        reli = []
        for i in range(len(eli)):
            reli.append(eli[-i-1])

        if eli == reli:
            return True
        return False
