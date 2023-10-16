class Solution:
    def reverseWords(self, s: str) -> str:
        mod_s = s.split()
        print(mod_s)
        left, right = 0, len(mod_s) - 1
        # double pointer loop
        while left <= right:
            mod_s[left], mod_s[right] = mod_s[right], mod_s[left]
            left += 1
            right -= 1
        # removed manual trimming as split() handles that            
        return ' '.join(mod_s)