class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if array is empty return 0
        if len(nums) == 0:
            return 0
        # set up index counter 
        i = 0
        # loop starting at 1 with j comparing to left neighbor i at 0
        for j in range(1, len(nums)):
            # if the number at i is not equal to the number at j
            if nums[j] != nums[i]:
                # increment i
                i += 1
                # set the number at i to the number at j
                nums[i] = nums[j]
        return i + 1
        