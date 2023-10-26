class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringified_x = str(x)
        left, right = 0, len(stringified_x) - 1
        while left <= right:
            if stringified_x[left] != stringified_x[right]:
                return False
            left+=1
            right-=1
        return True
        