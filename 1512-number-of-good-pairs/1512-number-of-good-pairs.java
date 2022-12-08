class Solution {
    public int numIdenticalPairs(int[] nums) {
//        start counter:
        int counter = 0;
//        loop through nums:
        for (int i=0 ; i<nums.length; i++) {
//            loop thought nums again, starting at i right neighbor:
            for (int j=i+1; j<nums.length; j++) {
                if (nums[i] == nums[j]) {
                    counter += 1;
                }
            }
        }
        return counter;
    }
}