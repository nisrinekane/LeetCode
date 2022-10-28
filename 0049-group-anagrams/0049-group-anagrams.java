class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //        edge case
        if (strs.length == 0) return new ArrayList();
//        declare a hashmap
        Map<String, List> hash = new HashMap<String, List>();
//        loop through strings
        for (String s : strs) {
//            conver string to array of characters
            char[] ca = s.toCharArray();
//            sort the characters array
            Arrays.sort(ca);
//            convert sorted array to string
            String key = String.valueOf(ca);
//            if key is not in the hashmap add it
            if (!hash.containsKey(key)) hash.put(key, new ArrayList());
//            add the string to the list of the key
            hash.get(key).add(s);
        }
//        return only the vals of hashmap
        return new ArrayList(hash.values());
    }
}