class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                return [i, seen[difference]]
            else:
                seen[nums[i]] = i
            
        