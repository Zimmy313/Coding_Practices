# C++ Misc Notes

## 1) References vs Pointers

Both can refer to another object, but they are not the same.

### Reference (`T&`)
- Must be initialized when declared.
- Cannot be reseated to refer to a different object.
- Used like an alias (no explicit dereference syntax).
- Cannot be null in normal usage.

```cpp
int a = 10;
int b = 20;

int& r = a;   // must bind now
r = 15;       // changes a
// r = b;     // assigns b's value into a, does NOT rebind r
```

### Pointer (`T*`)
- Stores an address.
- Can be reseated.
- Can be `nullptr`.
- Requires `*` to dereference.

```cpp
int a = 10;
int b = 20;

int* p = &a;
*p = 15;      // changes a
p = &b;       // now points to b
```

## 2) Pass-by-Value vs Reference vs Pointer

```cpp
void byValue(int x) { x += 1; }             // caller unchanged
void byRef(int& x) { x += 1; }              // caller value changes
void byPtr(int* x) { if (x) *x += 1; }      // explicit nullable/mutable handle
```

### Reference Example: `std::vector` Without Copy
Compare the following 3 functions that takes in different type of arguement.
```cpp
#include <iostream>
#include <vector>

void printByValue(std::vector<int> v) {
    std::cout << "by value addr:     "
              << static_cast<const void*>(v.data()) << '\n';
}

void printByConstRef(const std::vector<int>& v) {
    std::cout << "by const ref addr: "
              << static_cast<const void*>(v.data()) << '\n';
}

void appendByRef(std::vector<int>& v, int x) {
    v.push_back(x); // modifies caller's vector
}

int main() {
    std::vector<int> nums{1, 2, 3};

    std::cout << "caller addr:       "
              << static_cast<const void*>(nums.data()) << '\n';

    printByValue(nums);      // copy is made (different vector object)
    printByConstRef(nums);   // no copy (same vector object)

    appendByRef(nums, 4);
    std::cout << "size after appendByRef: " << nums.size() << '\n'; // 4
}
```

Reading the output:
- `caller addr` and `by const ref addr` should match.
- `by value addr` is from the copied vector.


## 4) `++i` vs `i++`

### Prefix increment: `++i`
- Increment first.
- Expression value is the incremented value.
- Usually preferred for iterators/user-defined types (can avoid extra temporary objects).

### Postfix increment: `i++`
- Expression value is the old value.
- Increment happens after.

```cpp
int i = 3;
int x = ++i;  // i = 4, x = 4

int j = 3;
int y = j++;  // y = 3, j = 4
```

### Out-of-bounds case (important)

```cpp
int arr[3] = {10, 20, 30};

int i = 0;
while (++i < 3) {
    // i: 1, 2  -> arr[1], arr[2] (safe)
    (void)arr[i];
}

i = 0;
while (i++ < 3) {
    // body sees i: 1, 2, 3 -> arr[3] is out of bounds
    (void)arr[i];
}
```

Reason: in `i++ < 3`, comparison uses old `i`, then `i` increments before body executes.
