class Solution {
    public int numIdenticalPairs(int[] nums) {
//       solving with hashmap:
        HashMap<Integer, Integer> map = new HashMap<>();
        int count = 0;
//         loop through nums:
        for (int i = 0; i < nums.length; i++) {
//             if map contains this num
            if (map.containsKey(nums[i])) {
//                 increment counter first with value of number in map !important
                count += map.get(nums[i]);
                System.out.println(map.get(nums[i]));
                map.put(nums[i], map.get(nums[i]) + 1);
            } else {
                map.put(nums[i], 1);
            }
        }
        return count;
    }
}