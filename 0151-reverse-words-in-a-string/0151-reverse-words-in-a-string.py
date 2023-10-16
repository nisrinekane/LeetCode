class Solution:
    def reverseWords(self, s: str) -> str:
        #first solution
        # mod_s = s.split()
        # print(mod_s)
        # left, right = 0, len(mod_s) - 1
        # # double pointer loop
        # while left <= right:
        #     mod_s[left], mod_s[right] = mod_s[right], mod_s[left]
        #     left += 1
        #     right -= 1
        # # removed manual trimming as split() handles that            
        # return ' '.join(mod_s)
        
        # more optimized solution:        
        mod_s = s.split()
        mod_s = mod_s[::-1]  
        return ' '.join(mod_s)