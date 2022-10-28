class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort numbers and declare result array
        nums.sort()
        result = []
        # iterate through numbers 
        for i in range(len(nums)-1):
            # skip if i is the same val as neighboring number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # set left and right pointers
            left = i+1
            right = len(nums)-1
            # iterate through both ways
            while left < right:
                # assign to a temporaty varibable the sum of three values (i, left: right of i and right: coming from end of loop)
                total = nums[i] + nums[left] + nums[right]
                # if total is negative continur to the right
                if total < 0:
                    left += 1
                # if total is positive continue to the left
                elif total > 0:
                    right -= 1
                # if they equal zero, add those values to the result
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    #  this to skip more duplicates in edge cases, code will work without lines 28-31 but wont pass leetcode test cases
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
