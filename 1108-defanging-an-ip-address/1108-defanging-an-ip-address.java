class Solution {
    public String defangIPaddr(String address) {
//         set result string
        String defangedIP = "";
//         loop over address:
        for (int i=0; i<address.length(); i++) {
//             store current character:
            char IP = address.charAt(i);
//             check if dot:
            if (IP == '.') {
                defangedIP = defangedIP + "[.]";
            } else {
                defangedIP = defangedIP + IP;
            }
        }
        return defangedIP;
    }
}