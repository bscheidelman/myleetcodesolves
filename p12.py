class Solution(object):
    def intToRoman(self, num):
        #Runtime: 46 ms
        #Memory: 13.5 MB
        
        output = ""
        li = [[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],[100,"C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]]
        for pair in li:
            while num >= pair[0]:
                output += pair[1]
                num -= pair[0]
        return output
