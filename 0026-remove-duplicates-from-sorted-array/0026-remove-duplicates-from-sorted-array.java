class Solution {
    public int removeDuplicates(int[] nums) {
//        if empty return 0
        if (nums.length == 0) return 0;
//        set up a counter index
        int i = 0;
//        loop through nums with j starting at 1
        for (int j = 1; j < nums.length; j++) {
//            if element on right and element on left arent equal
            if (nums[j] != nums[i]) {
//                increment index counter
                i++;
//                move index to right (j)
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
}