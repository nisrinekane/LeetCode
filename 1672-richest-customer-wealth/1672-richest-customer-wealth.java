class Solution {
    public int maximumWealth(int[][] accounts) {
//         brute force approach:
        //         instantiate largest amount:
        int largestAmount = 0;
//        loop through accounts:
        for (int i=0; i<accounts.length; i++) {
//            instantiate sum:
            int sum = 0;
//            loop through nested accounts:
            for (int j=0; j<accounts[i].length; j++) {
//                add element value to sum:
                sum += accounts[i][j];
            }
//            if sum is greater than largest amount:
            if (sum > largestAmount) {
//                set largest amount to sum:
                largestAmount = sum;
            } 
        }
        return largestAmount;
    }
}