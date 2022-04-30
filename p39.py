class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #Runtime: 4604 ms
        #Memory: 430.3 MB
        
    
        import itertools
        x = int(target/min(candidates)) + 1 
        li = []
        for counter in range(x):
            counter += 1
            combos = [p for p in itertools.product(candidates, repeat=counter)]
            for pair in combos:
                if sum(pair) == target:
                    temp = sorted(pair)
                    li.append(temp)
            for val in candidates:
                if val + min(candidates) * (counter) > target:
                    candidates.remove(val)
        tpls = [tuple(x) for x in li]
        dct = list(dict.fromkeys(tpls))
        dup_free = [list(x) for x in dct]
        return dup_free    
