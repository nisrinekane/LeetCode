import java.util.*;
import java.lang.Integer;
class Solution {
    public int[] twoSum(int[] nums, int target) {
//         new hashmap
        Map<Integer, Integer> map = new HashMap<>();
//         loop over nums
        for (int i=0; i<nums.length; i++) {
//             find difference between current element of num and target
            int difference = target - nums[i];
//             if difference exists in map
            if (map.containsKey(difference)) {
//                 return  index of number representing difference and current index
                // idky .add doesnt work to append the values to an array
                return new int[] {map.get(difference), i};
            } 
//             else add it to hashmap
            map.put(nums[i], i);
        }
//         return null if no solution
        return null;
    }
}