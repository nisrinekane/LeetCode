class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i:nums) {
            if (i != val) {
//                 reminder when using short for loop, no need for []
//                  couldve saved 5 mins
                nums[k] = i;
                k++;
            }
        }
        return k;
    }
}