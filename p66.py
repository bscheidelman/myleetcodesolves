class Solution(object):
    def plusOne(self, digits):
        #Runtime: 20 ms
        #Memory: 13.3 MB
    
    
        a = -1
        if digits.count(9) == len(digits):
            li = []
            li.append(1)
            for counter in range(len(digits)):
                li.append(0)
            return li
        if digits[a] == 9:
            while digits[a] == 9:
                digits[a] = 0
                a = a -1
        digits[a] = digits[a] + 1
        return digits
