class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a dictionary
        dict = {}
        #loop through the list
        for i in strs:
            #sort the word:
            sorted_word = ''.join(sorted(i))
            # if the sorted word is not in the dictionary, add it as key with the original string as value
            if sorted_word not in dict:
                dict[sorted_word] = [i]
            # if the sorted word is in the dictionary, add the word as a value to the existing key
            else:
                dict[sorted_word].append(i)
            # convert the dictionary to a list of lists and return its values
        return list(dict.values())   