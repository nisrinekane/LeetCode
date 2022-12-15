class Solution {
    public int majorityElement(int[] nums) {
//         instantiate map
       HashMap<Integer, Integer> map = new HashMap<>();
//         loop over nums:
        for (int i:nums) {
//             if key exist in map
            if (map.containsKey(i)) {
//                 increment its value
                map.put(i, map.get(i) + 1);
            } else {
//                 else, instantiate it
                map.put(i, 1);
            }
        }
        
//      instantiate variable for key and one for its value:
        int k = 0;
        int v = 0;
        for (int i:map.keySet()) {
            if (map.get(i) > v) {
                v = map.get(i);
                k = i;
            }
        }
        return k;
    }
}