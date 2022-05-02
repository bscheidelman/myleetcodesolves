class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dcount= [letter for letter in s if s.count(letter) > 1]
        if dcount == []:
            return len(s)
        lirep = []
        ans = []
        duplicates_guess = [letter for letter in s if s.count(letter) > 1]
        unique_dupe = list(set(duplicates_guess))
        temp = s
        for val in unique_dupe:
            tli = []
            for let in temp:
                if let == val:
                    tli.append(temp.index(let))
                    temp = temp[0:temp.index(let)] + "*" + temp[temp.index(let)+1:len(temp)]
            lirep.append(tli)
        for li in lirep:
            for val in range(len(li)):
                if val == len(li) - 1:
                    dcount= [letter for letter in s[li[0]:li[val]] if s[li[0]:li[val]].count(letter) > 1]
                    if dcount == []:
                        ans.append(len(s[li[0]:li[val]+1]))
                else:
                    dcount= [letter for letter in s[li[val]:li[val+1]] if s[li[val]:li[val+1]].count(letter) > 1]
                    if dcount == []:
                        ans.append(len(s[li[val]:li[val+1]+1]))
        end = 0               
        for let in s:
            init = 0
            dcount= [letter for letter in s[init:end] if s[init:end].count(letter) > 1]
            if dcount == []:
                ans.append(len(s[init:end+1]))
            else:
                break
            end += 1
        init = len(s) - 1               
        for let in s:
            init = len(s) - 1
            dcount= [letter for letter in s[init:end] if s[init:end].count(letter) > 1]
            if dcount == []:
                ans.append(len(s[init:end+1]))
            else:
                break
            init -= 1
            
        
        if len(ans) > 0:
            return max(ans)    
        else:
            return 0
