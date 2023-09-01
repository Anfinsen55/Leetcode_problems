class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = -1
        su=0
        if s=="":
            return(True)
        for i in range(len(s)):
            if s[i] not in t:
                return(False)
            for j in range(index+1,len(t)):
                if s[i]==t[j]:
                    index = j
                    su +=1
                    break

        if su == len(s):
            return(True)
        
        else:
            return(False)
                

