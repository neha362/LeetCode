#Merge Strings Alternatively, solved Oct 12 2024
class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder x = new StringBuilder();
        int y = Math.min(word1.length(), word2.length());
        for(int i = 0; i < y; i++) {
            x.append(word1.charAt(i));
            x.append(word2.charAt(i));
        }
        x.append(word1.substring(y));
        x.append(word2.substring(y));
        return x.toString();
    }
}
