class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # edge case for empty array:
        if not candies:
            return []

        # find the maximum candy kid assuming it's the first
        # you can also use built-in max
        max_candy = candies[0]
        for candy in candies:
            if candy > max_candy:
                max_candy = candy

        result_array = []
        # if total candies at current i is bigger/equal than biggest val 
        # return true, else false
        for candy in candies:
            if candy + extraCandies >= max_candy:
                result_array.append(True)
            else:
                result_array.append(False)

        return result_array