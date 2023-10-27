class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s=list(s)
        count=0
        vowel=set("AEIOUaeiou")
        max_vowel=0
        for i in range(k):
            if s[i] in vowel:
                count+=1
        max_vowel=count
        for i in range(k,len(s)):
            if s[i-k] in vowel:
                count-=1
            if s[i] in vowel:
                count+=1
            max_vowel=max(max_vowel,count)
        return max_vowel
