class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # edge case
        if len(nums) < 3:
            return False
        
        first = nums[0]
        second = None 
        
        # loop through list from the right
        for n in nums[1:]:
            # maintain two numbers: first is the smallest found 
            # and second is the smallest found greater than first
            # keep replacing after each new find 
            # if we find any num larger than both, we have our triplet.
            if second is not None and n > second:
                return True
            elif n <= first:
                first = n
            elif second is None or n <= second:
                second = n

        return False
