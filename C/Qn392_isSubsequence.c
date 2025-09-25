#include <string.h>
#include <stdbool.h>

bool isSubsequence(char* s, char* t) {
    int left = 0, right = 0, n = strlen(t), m = strlen(s);

    while (left < m && right < n){
        char left_c = s[left], right_c = t[right];
        
        if (left_c == right_c){
            left++;
        }
        right++;
    }
    return left==m;

}