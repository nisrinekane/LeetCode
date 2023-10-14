class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        len1 = len(word1)
        len2 = len(word2)
        
        for i in range(min(len1, len2)):
            result += word1[i]
            result += word2[i]
            
#         if first word is longer than second
        if len1>len2:
#         append characters from word1 starting where word2 stops
            result += word1[len2:]
#          same concept if second word is longer than first
        else:
            result += word2[len1:]
            
        return result
            