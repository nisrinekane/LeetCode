class Solution:
    def romanToInt(self, s: str) -> int:
        #set up a hashmap
        values = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result = 0
        for i in range(len(s)):
            # if this item is not the last item and is smaller than next item val
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]] :
                result = result - values[s[i]]                      
                # then subtract current item val from result
            else:
                # else add current item val to result
                result = result + values[s[i]]                      
        return result
        
