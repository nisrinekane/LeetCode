import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

// solution using hashmap
class Solution {
    public boolean isValid(String s) {
//        initiate hashmap:
        Map<Character, Character> map = new HashMap<>();
//       add brackets to map:
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');
//        initiate stack:
        Stack<Character> stack = new Stack<>();
//         edge case:
        if (s.length() % 2 != 0) {
            return false;
        }
//        loop over string:
        for (int i = 0; i < s.length(); i++) {
//            if the current char is a key in the map i.e"[":
            if (map.containsKey(s.charAt(i))) {
//                push its val to stack i.e"]"
                stack.push(map.get(s.charAt(i)));
            } else {
//                if cur char is not a key in the map (closing bracket) then:
//                if stack is empty or the curr char is not equal to the top of the stack:
                if (stack.isEmpty() || s.charAt(i) != stack.pop()) {
//                    return false
                    return false;
                }
            }
        }
//        if the stack is empty return true: (simplified if/else)
        return stack.isEmpty();
    }
}