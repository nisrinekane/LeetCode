class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
#         2 pointers to close to divide and conquer
        left, right = 0, len(nums) - 1
    
        while left <= right:
#             integer division, start at middle
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
#             if we cant find it, place where it should have been
#             when loop end, right is at the left of the target's position
#             left indicates the target's location or insertion point
        return left
                
        