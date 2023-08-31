class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=''.join(filter(str.isalnum, s))
                
        s=list(s)
        rev1="".join(s)
        s.reverse()
        a="".join(s)
                
                

        if a==rev1:
            return(True)
        elif a=="":
            return(True)

        else:
            return(False)
