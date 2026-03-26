/*
=============================================================
Cpp Common Functions & Formatting Cheat Sheet
=============================================================
*/

#include <string>
#include <iostream>
using namespace std; // lets you write cout, cin, string without std::

void demo_string() {

    // illustrate I/O
    string s, t;
    cout << "Please input string s:\n";
    cin >> s;
    cout << "Please input string t:\n";
    cin >> t;

    // playing with string
    cout << s.size() << "\n";
    cout << (s == t) << "\n"; // () is important due to precedence rule. 
    // compare the 2 string using '==' directly
}

int main(){
    demo_string();
    
    return 0;
}