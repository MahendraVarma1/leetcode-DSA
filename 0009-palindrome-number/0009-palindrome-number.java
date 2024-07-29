class Solution {
    public boolean isPalindrome(int x) {
        int test = x;
        int d=0;
        if (x<0){
            return false;
        }
        while (x!=0) {
            d = d*10 + x%10;
            x = (int)(x/10);
        }
        if (test == d) {
            return true;
        }
        return false;
    }
}