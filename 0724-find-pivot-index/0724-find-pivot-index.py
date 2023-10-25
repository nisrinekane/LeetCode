class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        left_sum = 0
        index = 0
        for num in nums:
            if nums_sum - left_sum - num == left_sum:
                return index
            left_sum += num
            index += 1
        return -1
            