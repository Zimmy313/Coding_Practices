/*
=============================================================
C Common Functions & Formatting Cheat Sheet
=============================================================
*/

#include <stdio.h>   
#include <ctype.h>  
#include <math.h>  

// =====================================
// ctype.h
// =====================================
void ctype_demo() {
    char c = 'A';
    printf("isalpha: %d\n", isalpha(c));
    printf("isdigit: %d\n", isdigit('9'));
    printf("tolower: %c\n", tolower(c));
    printf("toupper: %c\n", toupper('b'));
    printf("isspace: %d\n", isspace(' '));
}

// =====================================
// math.h
// =====================================
void math_demo() {
    printf("sqrt(9) = %.2f\n", sqrt(9.0));
    printf("pow(2,3) = %.2f\n", pow(2,3));
    printf("fabs(-5.5) = %.2f\n", fabs(-5.5));
    printf("floor(2.9) = %.0f\n", floor(2.9));
    printf("ceil(2.1) = %.0f\n", ceil(2.1));
    printf("fmax(10,20) = %.0f\n", fmax(10,20));
    printf("fmin(10,20) = %.0f\n", fmin(10,20));
}

// =====================================
// stdio.h - Formatting Reference
// =====================================
void formatting_demo() {
    int a = 42;
    double pi = 3.14159265;
    char ch = 'Z';
    char str[] = "LeetCode";

    // Integers
    printf("Integer: %d\n", a);          // default
    printf("Integer (width 5): %5d\n", a);   // right aligned
    printf("Integer (pad with 0): %05d\n", a);

    // Floating point
    printf("Float (2 decimals): %.2f\n", pi);
    printf("Float (scientific): %.3e\n", pi);
    printf("Float (width 8, 3 decimals): %8.3f\n", pi);

    // Characters and strings
    printf("Character: %c\n", ch);
    printf("String: %s\n", str);
    printf("String (width 10): %10s\n", str);     // right align
    printf("String (left align): %-10s\n", str);  // left align

    // Mix of types
    printf("Mix: int=%d, char=%c, string=%s, float=%.2f\n", a, ch, str, pi);
}

// =====================================
// stdio.h - Input Reference
// =====================================
void input_demo() {
    int num;
    double val;
    char c;
    char word[100];

    printf("Enter an int, double, char, and word: ");
    scanf("%d %lf %c %s", &num, &val, &c, word);

    printf("You entered -> int:%d, double:%.2f, char:%c, word:%s\n", num, val, c, word);
}

// =====================================
// Main
// =====================================
int main() {
    ctype_demo();
    math_demo();
    formatting_demo();
    input_demo();
    return 0;
}