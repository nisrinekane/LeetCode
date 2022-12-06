class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        // instantiate a hashmap to count occurrences
        HashMap<Integer, Integer> hashmap1 = new HashMap<Integer, Integer>();
        // loop over the array:
        for (int i=0; i<arr.length; i++) {
            // check if current elem exist in hashmap1
            if (hashmap1.containsKey(arr[i])) {
                // yes: get key, get current its value and increment it
                hashmap1.put(arr[i], hashmap1.get(arr[i]) + 1);
            } else {
                // if not, add it at count of 1
                hashmap1.put(arr[i], 1);
            } 
        }
        // instantiate second hash and set values from hash1 as keys of hash2
        // to check for unique count 
        HashMap<Integer, Boolean> hashmap2 = new HashMap<Integer, Boolean>();
        // loop over hashmap1's keys (numbers):
        for (int i : hashmap1.keySet()) {
            // check if its values exists in hashmap2:
            if (hashmap2.containsKey(hashmap1.get(i))) {
                // if yes, count is repeating so return false
                return false;
            } else {
                // if no, add count from hash1 to hash2 as key
                // value can be anything
                hashmap2.put(hashmap1.get(i), true);
            }
        }
        // default: true
        return true;
    }
}