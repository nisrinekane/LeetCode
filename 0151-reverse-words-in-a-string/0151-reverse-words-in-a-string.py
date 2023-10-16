class Solution:
    def reverseWords(self, s: str) -> str:
        # second solution, testing for optimization         
        mod_s = s.split()
        mod_s = mod_s[::-1]  
        return ' '.join(mod_s)