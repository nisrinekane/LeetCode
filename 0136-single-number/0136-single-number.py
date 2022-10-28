class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # create a dictionary
        dict = {}
        # loop through the list
        for i in nums:
            # if the number is not in the dictionary, add it
            if i not in dict:
                dict[i] = 1
            # if the number is in the dictionary, remove it
            else:
                dict.pop(i)
        # return the number that is left in the dictionary
        return dict.popitem()[0]