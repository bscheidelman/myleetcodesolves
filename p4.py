class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Runtime: 143 ms
        #Memory: 14.1 MB
        nli = nums1 + nums2
        nli.sort()
        if len(nli) % 2 == 1:
            return nli[int(((len(nli)-1)/2))]
        else:
            x = nli[int(len(nli)/2 - 1)] + nli[int(len(nli)/2)]
            return x/2
        
