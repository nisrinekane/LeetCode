class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
    # instantiate result to stop function once it reaches n value
        result = 0
    # using flower[i]=1 prevents double couting        
        for i in range(len(flowerbed)):
            # only check if current plot is empty
            if flowerbed[i] == 0:
                # handle first plot
                if i == 0 and (len(flowerbed) == 1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    result += 1
                # handle  middle plots
                elif 0 < i < len(flowerbed) - 1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    result += 1
                # handle the last plot
                elif i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    result += 1
        # if result value satisfies n return true           
        return result >= n
                       
        