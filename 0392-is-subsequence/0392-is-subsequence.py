class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_pointer, main_pointer = 0, 0
        while sub_pointer < len(s) and main_pointer < len(t):
            if s[sub_pointer] == t[main_pointer]:
                sub_pointer+=1
            main_pointer+=1
        if sub_pointer == len(s):
            return True
        return False