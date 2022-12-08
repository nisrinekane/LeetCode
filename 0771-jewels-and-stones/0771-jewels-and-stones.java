import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
    public int numJewelsInStones(String jewels, String stones) {
//        optimized solution with  regex  
//        instantiate the pattern to look through
        Pattern pattern = Pattern.compile("[" + jewels + "]");
//        instantiate match to look for
        Matcher matcher = pattern.matcher(stones);
//        instantiate counter
        int count = 0;
//        while there is a match, increment counter
        while (matcher.find()) {
            count++;
        }
        return count;
    }
}