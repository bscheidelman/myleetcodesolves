# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        li1 = []
        li2 = []
        for pair in [[l1,li1],[l2,li2]]:
            while pair[0]:
                if pair[0]:
                    temp = pair[0].val
                    pair[1].append(temp)
                if pair[0]:
                    pair[0] = pair[0].next
                else:
                    pair[0] = None

        lengthlist = [len(li1),len(li2)]
        alt = [li1,li2]
        while len(li1) != len(li2):
            alt[lengthlist.index(min(lengthlist))].append(0)
        
        sumli = []
        for val in range(len(li1)):
            sumli.append(li1[val] + li2[val])
        
        for val in range(len(sumli)-1):
            if sumli[val] >= 10:
                sumli[val+1] += 1
                sumli[val] -= 10

        if sumli[-1] >= 10:
            sumli[-1] -= 10
            sumli.append(1)
        
        #(MISSING) need to return in proper type --> form of NodeLength Object
        rval = sumli
        print(rval)
                
        
        
