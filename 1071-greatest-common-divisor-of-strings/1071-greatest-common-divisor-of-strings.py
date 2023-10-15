class Solution:
     def gcdOfStrings(self, str1: str, str2: str) -> str:
            # first make sure that the str is repeatable and correct
        if str1 + str2 != str2 + str1:
            return ""

        # use gcd onof the lengths of str1 and str2
        gcd_length = math.gcd(len(str1), len(str2))

        # answer is the prefix of either str1 or str2 of length gcd_length
        return str1[:gcd_length]
        
