#include <ctype.h> 

bool isPalindrome(char* s) {
    int left = 0, right = strlen(s)-1;

    while(left < right){

        while(left<right && !isalnum(s[left])){
            left++;
        }
        while(left<right && !isalnum(s[right])){
            right--;
        }
        char left_c = tolower(s[left]), right_c = tolower(s[right]);
        if(left_c == right_c){
            left++; right--;
        }
        else{
            return false;
        }
    }
    return true;
}