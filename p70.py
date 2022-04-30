class Solution(object):
    def climbStairs(self, n):
        #Runtime: 8 ms
        #Memory: 13.5 MB
        
        li = [1,1,1]
        length = n
        if n <= 3:
            return n
        while len(li) < length:
            temp = li[len(li)-1] + li[len(li)-2]
            li.append(temp)
        return sum(li)
        
