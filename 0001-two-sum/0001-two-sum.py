class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through list
        for i in range(len(nums)):
            #loop through rest
            for j in range(i+1,len(nums)):
                # add up i to each num and test
                if nums[i]+nums[j]==target:
                    return [i,j]