class Solution {
    public List<String> fizzBuzz(int n) {
        //     initiate an empty list
        List<String> list = new ArrayList<>();
//        loop over n:
        for (int i = 1; i <= n; i++) {
//            if i is divisible by 3 and 5
            if (i % 3 == 0 && i % 5 == 0) {
//                add FizzBuzz to list
                list.add("FizzBuzz");
            } else if (i % 3 == 0) {
//                if i is divisible by 3 
//                add Fizz to list
                list.add("Fizz");
            } else if (i % 5 == 0) {
//                if i is divisible by 5
//                add Buzz to list
                list.add("Buzz");
            } else {
//                if i is not divisible by 3 or 5
//                add i to list
                list.add(String.valueOf(i));
            }
        }
        return list;
    }
}