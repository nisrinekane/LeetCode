class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap solution:
        hashmap = {}
        for i in range(len(nums)):
#             store difference between target and current element 
            difference = target - nums[i]
#     if the value exists in hash, return current element and difference
            if difference in hashmap:
                return [i, hashmap[difference]]
#                 default: add current element' to hashmap
            hashmap[nums[i]] = i