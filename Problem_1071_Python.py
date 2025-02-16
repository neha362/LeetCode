#Greatest Common Divisor of Strings, solved Oct 12 2024
class Solution {
    public String gcdOfStrings(String str1, String str2) {
        String match = (str1.length() < str2.length()? str1 : str2);
        while (match.length() > 0) {
            if(str1.length() % match.length() == 0 && str1.length() % match.length() == 0) {
                if (str1.equals(match.repeat(str1.length()/match.length())) &&
                str2.equals(match.repeat(str2.length()/match.length())))
                    return match;
            }
            match = match.substring(1);
        }
        return "";
    }
}
