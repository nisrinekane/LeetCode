class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
#       convert str to list
        mod_str = list(s)
#       set left pointer
        left_pointer = 0
#       set right pointer
        right_pointer = len(mod_str)-1
#       start loop on left till middle:
        while left_pointer < right_pointer:
#             if char at left pointer not a vowel, increment:
            if mod_str[left_pointer] not in vowels:
                left_pointer += 1
#             same but for right pointer, decrement:
            elif mod_str[right_pointer] not in vowels:
                right_pointer -= 1
#             if both pointers are vowels switch
            else:
                mod_str[left_pointer], mod_str[right_pointer] = mod_str[right_pointer], mod_str[left_pointer]
                left_pointer += 1
                right_pointer -= 1
        return ''.join(mod_str)        