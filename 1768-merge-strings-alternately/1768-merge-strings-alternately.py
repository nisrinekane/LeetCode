class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        biggest_str = max(len(word1), len(word2))
        result = ''
        i = 0
        while i < biggest_str:
#             check and add both instantaneously 
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
            i+=1
        return result
        