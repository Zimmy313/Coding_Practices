/*
=============================================================
Cpp Common Functions & Formatting Cheat Sheet
=============================================================
*/

#include <string>
#include <iostream>
#include <vector>
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
    cout << (s == t) << "\n"; // () is important due to precedence rule. Compare the 2 string using '==' directly
    cout << (s.find("a") != string::npos) << "\n"; // returns the first occurance of the character. npos is a static member constatn to indicate an invalid or "no position" result

}

void demo_vector() {
    vector<int> v = {1, 2, 3, 4, 5};

    cout << v[0] << "\n"; // access the first element
    cout << v.back() << "\n"; // access the last element, this returns a reference to the last element, so you can modify it
    v.front() = 0; // access the first element and modify it, this returns a reference to the first element, so you can modify it

    v.push_back(6); // add an element to the end of the vector
    v.pop_back(); // remove the last element of the vector, this does not return the removed element, it just removes it from the vector
    v.clear(); // remove all elements from the vector, this does not change the capacity of the vector, it just sets the size to 0
    
    cout << v.size() << "\n";
}

int main(){
    demo_string();
    demo_vector();
    
    return 0;
}