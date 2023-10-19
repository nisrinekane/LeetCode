class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # solve using two pointers
        left, right = 0, 0  # Initialize two pointers
        #start loop from the end
        while right < len(nums):
            # if the right pointer is not zero but the left pointer is zero
            if nums[right] != 0 and nums[left] == 0:
                # swap the values
                nums[left], nums[right] = nums[right], nums[left]
                # increment the left pointer
                left += 1
            # if the right pointer is not zero and the left pointer is not zero
            if nums[right] != 0 and nums[left] != 0:
                # increment the left pointer
                left += 1
            # increment the right pointer
            right += 1