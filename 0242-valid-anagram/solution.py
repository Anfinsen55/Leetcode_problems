class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return not (Counter(s)-Counter(t)) and len(s)==len(t)
