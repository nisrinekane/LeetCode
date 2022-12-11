class Solution {
    public int[] shuffle(int[] nums, int n) {
        //        instantiate result array:
        int[] res = new int[nums.length];
//        instantiate counter:
        int counter = 0;
//        loop through nums:
        for (int i=0; i<n; i++) {
//            add element at index of i to result array:
            res[counter] = nums[i];
//            increment counter:
            counter++;
//            add element at index of i+n to result array:
            res[counter] = nums[i+n];
//            increment counter:
            counter++;
        }
        return res;
    }
}