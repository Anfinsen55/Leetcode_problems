class Solution:
    def reverseWords(self, s: str) -> str:
        new=s.split()
        final=""
        for i in range(len(new)):
            final+=new[len(new)-1-i]+" "
        return(final.strip())        
