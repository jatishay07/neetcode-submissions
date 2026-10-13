class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return strs
        
        anagram = {}

        for str in strs:
            char = [0]*26

            for ch in str:
                char[ord(ch) - ord('a')]+=1

            if tuple(char) not in anagram:
                anagram[tuple(char)] = [str]
            else: 
                anagram[tuple(char)].append(str)

        return list(anagram.values())