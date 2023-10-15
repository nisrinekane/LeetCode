class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        resultArr = []
        for i in candies:
            bool = True
            for j in candies:
                if i + extraCandies < j:
                    bool = False
                    break
            resultArr.append(bool)
        return resultArr