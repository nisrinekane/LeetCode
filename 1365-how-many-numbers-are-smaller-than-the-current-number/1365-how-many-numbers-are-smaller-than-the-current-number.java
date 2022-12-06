class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
//    optimized solution
//        clone array:
        int[] nums2 = nums.clone();
//        sort array:
        Arrays.sort(nums2);
//        initiate hashmap:
        HashMap<Integer, Integer> hashmap = new HashMap<Integer, Integer>();
//        loop over array:
        for (int i = 0; i < nums2.length; i++) {
//            if hashmap does not contain the current element (number):
            if (!hashmap.containsKey(nums2[i])) {
//              add it as key to the hashmap, the value is its index
                hashmap.put(nums2[i], i);
            } else {
//                 do not increment! will break with reoccurring numbers
                continue;
            }
        }
//        loop over original array:
        for (int i = 0; i < nums.length; i++) {
//            change current element to the value of the current element in the hashmap
            nums[i] = hashmap.get(nums[i]);
        }
//        return array
        return nums;
    }
}

    
