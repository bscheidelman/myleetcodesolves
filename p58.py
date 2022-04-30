class Solution(object):
    def lengthOfLastWord(self, s):
        #Runtime: 15 ms
        #Memory: 13.7 MB
        
        
        if s.isalpha() == True:
            return len(s)
        eindex = -1
        while s[eindex].isalpha() == False:
            eindex -= 1
        sindex = eindex
        while s[sindex].isalpha() == True:
            sindex -= 1
            if sindex * -1 > len(s):
                break
        return sindex*-1 - eindex * -1
