class Solution {
    public boolean isAnagram(String s, String t) {
//        edge case:
        if (s.length() != t.length()) {
            return false;
        }
//        instantiate a hashmap
        HashMap<Character, Integer> map = new HashMap<>();
//        loop through the first string and add each character to the hashmap
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
//        loop through the second string and subtract each character from the hashmap
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            if (map.containsKey(c)) {
                map.put(c, map.get(c) - 1);
            } else {
                return false;
            }
        }
//        loop through the hashmap and check if all values are 0
        for (int value : map.values()) {
            if (value != 0) {
                return false;
            }
        }
        return true;
    }
}