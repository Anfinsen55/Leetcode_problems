class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=''.join(filter(str.isalnum, s))
        left=0
        right=len(s)-1
        rev1=""
        for left in range(len(s)):
            rev1=rev1+s[right-left]

        if s==rev1:
            return(True)
        else:
            return(False)
