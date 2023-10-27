class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1= len(str1)
        l2= len(str2)
        ans="";
        if (str1[0]!=str2[0]):
            return ans
        gcd= min(str1,str2);
        for i in range(len(gcd),0,-1):
            gcdl= i
            if (l1%gcdl!=0 or l2%gcdl!=0):
                gcd= gcd[:-1]
                continue;
            if (l1<=l2):
                mini= int(l1/gcdl)
                maxi= int(l2/gcdl)
                if (mini*gcd==str1 and maxi*gcd==str2):
                    return gcd;  
                
            if (l1>l2):
                mini= int(l2/gcdl)
                maxi= int(l1/gcdl)
                if (mini*gcd==str2 and maxi*gcd==str1):
                    return gcd; 
            gcd= gcd[:-1]
        return ans;
