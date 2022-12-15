class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         instantiate a dictionary:
        dict = {}
#         loop over nums:
        for i in nums:
#         if it exists in dict, increment, else instantiate it
            if i in dict:
                dict[i] = dict[i] + 1
            else :
                dict[i] = 1
#                 set up k for result and v to hold the value
        k = 0;
        v = 0;
        for key in dict:
#             if the value of current key is bigger than v
            if dict[key] > v:
#         v will hold the new biggest value
                v = dict[key]
#     the new result is the current element or key
                k = key
#     return final key that holds greatest value
        return k
        