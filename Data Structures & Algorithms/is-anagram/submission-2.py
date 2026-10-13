class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char = [0]*26
        print(char)

        for i in range (len(s)):
            char[ord(s[i]) - ord('a')]+=1
            char[ord(t[i]) - ord('a')]-=1
        
        for num in char:
            if num != 0:
                return False
        return True
