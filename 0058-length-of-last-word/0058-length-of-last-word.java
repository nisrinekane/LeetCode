class Solution {
    public int lengthOfLastWord(String s) {
        String arr[] = s.split(" ");
        int counter = 0;
        String target = arr[arr.length-1];
        for (int i=0; i<target.length(); i++) {
            counter++;
        }
        return counter;
    }
}