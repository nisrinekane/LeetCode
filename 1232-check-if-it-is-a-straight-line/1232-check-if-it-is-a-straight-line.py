class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # edge case: only 1 point
        if len(coordinates)==2:
            return True
        else:
        #instantiate starting points             
            x1 = coordinates[0][0]
            y1 = coordinates[0][1]
            x2 = coordinates[1][0]
            y2 = coordinates[1][1]
            # loop through points starting at index 1
            for i in range(1,len(coordinates)):
                x = coordinates[i][0]
                y = coordinates[i][1]
            #slope formula: (y2-y1)/(x2-x1), division breaks code
            # neighbor index (y[i+1]-y[i]) doesnt work    
            # accidental correct answer:             
                if (y2-y1)*(x-x2)!=(y-y2)*(x2-x1):
                    return False
            return True