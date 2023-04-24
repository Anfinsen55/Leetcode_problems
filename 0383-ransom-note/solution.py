class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        string1, string2 = Counter(ransomNote), Counter(magazine)
        if string1 & string2 == string1:
            return True
        return False
