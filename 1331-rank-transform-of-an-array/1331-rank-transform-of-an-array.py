class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        #sort array
        sorted_arr = sorted(arr)
        # initialize rank to 1
        rank = 1
        # instantiate hash map
        rank_dict = {}
        # iterate through sorted array
        for n in range(len(sorted_arr)):
            # if element is not in hash map, add it
            if sorted_arr[n] not in rank_dict:
                rank_dict[sorted_arr[n]] = rank
                # increment rank each after each loop
                rank += 1
        # inside an array iterate through original array,use loop index to fetch the right hashmap key value
        return [rank_dict[i] for i in arr]