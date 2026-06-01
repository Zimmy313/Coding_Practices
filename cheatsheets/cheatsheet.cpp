/*
=============================================================
Cpp Common Functions & Formatting Cheat Sheet
=============================================================
*/

#include <string>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std; // lets you write cout, cin, string without std::

void demo_string() {
    string s, t, temp;
    char yolo;

    // illustrate I/O
    cout << "Please input string s:\n";
    cin >> s; // note that this only takes in the first input
    cout << "Please input string t:\n";
    getline(cin, t); // gets the entire line

    // playing with string
    cout << s.size() << "\n";
    cout << (s == t) << "\n"; // () is important due to precedence rule. Compare the 2 string using '==' directly
    cout << (s.find("a") != string::npos) << "\n"; // returns the first occurance of the character. npos is a static member constatn to indicate an invalid or "no position" result

    temp = s + t; // result is equal to s+= t 
    temp.push_back('c'); // needs a single character.
    temp.clear(); // temp is now ""

    yolo = s[0]; // no need casting. can use index deirectly

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

void demo_hashmaps(void) {
    // unordered_map and unordered_set are hash-table based.
    // Average lookup: O(1)
    // Worst-case lookup: O(n)

    unordered_map<string, int> student = {{"Bob", 1}, {"John", 2}};

    cout << student["Bob"]; 
    // You CAN use [] with unordered_map.
    // Key point: student["Bob"] accesses value by key, not by position/index.
    // student[0] does not mean first element.
    // note that accees by key will create the pair if not exist. use find instead if you dont want to create it. 

    student.insert({"Mike", 100});
    student["Alice"]; // creates Alice with default value

    // updating
    student.at("Mike") = 10000;
    student["Mike"] = 100;
    // Mike's value is now 100, because the second update overwrites the first one.

    // find() returns an iterator.
    // end() means "not found" when compared with find().
    // end() is a past-the-last marker, not a real element.
    if (student.find("Mike") != student.end()) {
        cout << "WooHOO!\n";
    }

    student.erase("Mike");
    student.clear(); // removes all key-value pairs

    if (student.empty()) {
        cout << "GG\n";
    }
}

int main(){
    demo_string();
    demo_vector();
    demo_hashmaps();

    // iostream
    cout << boolalpha; // a switch to print true/false instead of 1/0


    cout << endl; // flush the output, this may slow down process. not necessary.
    cout << '\n' << flush; // same as above
    
    return 0;
}