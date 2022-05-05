class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome(input_string):
            eli = []
            for x in input_string:
                eli.append(x)

            reli = []
            for i in range(len(eli)):
                reli.append(eli[-i-1])

            if eli == reli:
                return True
            return False
        ansli = []
        for val in range(len(s)):
            if s.count(s[val]) > 2:
                temp = s
                while temp[val+1:].__contains__(s[val]):
                    eindex = temp[val+1].index(s[val])
                    if check_palindrome(s[val:eindex+1]) == True:
                        ansli.append([len(s[val:eindex+1]),s[val:eindex+1]])
                    temp[eindex] = "*"
            eindex = val
            sindex = val
            while sindex >= 0 and eindex < len(s):
                if check_palindrome(s[sindex:eindex]) == True:
                    ansli.append([len(s[sindex:eindex]),s[sindex:eindex]])
                eindex += 1
                sindex -= 1
        hold = ""
        max = 0
        for pair in ansli:
            if pair[0] > max:
                max = pair[0]
                hold = pair[1]
        return hold
