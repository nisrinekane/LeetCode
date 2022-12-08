class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
//        set counter:
        int counter = 0;
//        loop through nums:
        for (int i=0; i<nums.size(); i++) {
//            loop through nums again:
            for (int j=i+1; j<nums.size(); j++) {
//                if match, increment counter
                if (nums[i] == nums[j]) {
                    counter++;
                } else {
                    continue;
                }
            }
        }
        return counter;
    }
};