class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l1=list(s)
        l2=list(t)
        for x in l2:
            if x in l1:
                l1.remove(x)
            else:
                return x
