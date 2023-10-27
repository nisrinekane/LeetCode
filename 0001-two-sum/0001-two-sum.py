class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for n in range(len(nums)):
#             calculate the amount needed to reach target
            difference = target - nums[n]
#     if the difference exists in sum
            if difference in seen:
#         return its index and the current index
                return [seen[difference], n]
#  add current number's index to dictionary
            seen[nums[n]] = n
            
        