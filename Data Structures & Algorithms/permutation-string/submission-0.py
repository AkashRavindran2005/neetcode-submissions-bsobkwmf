class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l  = 0
        temp = s1
        flag = False
        for r in range(len(s2)):
            if s2[l: r+1] in temp:
                l += 1
                temp2 = list(temp).remove(s2[l:r+1])
                temp = str(temp2)
                flag = True
            else:
                l += 1
                temp = s1
                flag = False
        return flag
        