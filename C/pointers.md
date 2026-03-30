# C Pointers: Practical Reference

## Core Model

- A pointer stores a memory address.
- Pointer type tells the compiler how to interpret bytes at that address.
- `*p` dereferences the pointer (access value at address).
- `&x` gets the address of object `x`.

Example:

```c
int x = 42;
int *p = &x;
printf("%d\n", *p);   /* 42 */
```

## Declaration Syntax (Read Right-to-Left)

```c
int *p;        /* p is pointer to int */
int **pp;      /* pp is pointer to pointer to int */
int *a[3];     /* a is array of 3 pointers to int */
int (*pa)[3];  /* pa is pointer to array of 3 int */
```

## Null, Wild, Dangling

- `NULL`: pointer intentionally points to no object.
- Wild pointer: uninitialized pointer (undefined behavior if dereferenced).
- Dangling pointer: points to memory that is no longer valid.

```c
int *p = NULL;        /* good */
int *q;               /* wild until initialized */
free(p);
p = NULL;             /* avoid dangling reuse pattern */
```

## Pointer Arithmetic

Arithmetic moves in units of pointed type:

```c
int arr[4] = {10, 20, 30, 40};
int *p = arr;         /* same as &arr[0] */
printf("%d\n", *(p + 2));  /* 30 */
```

`p + 1` for `int *` advances by `sizeof(int)` bytes.

## Arrays and Pointers (Important Distinction)

- Array name usually decays to pointer to first element in expressions.
- Array itself is not a pointer object.
- `sizeof(arr)` gives full array size, not pointer size.

```c
int arr[5];
int *p = arr;
sizeof(arr);   /* 5 * sizeof(int) */
sizeof(p);     /* size of pointer */
```

## Pointer to Pointer (`**`)

Used when a function must modify a pointer variable itself.

```c
void alloc_int(int **out) {
    *out = malloc(sizeof(**out));
    if (*out) **out = 123;
}
```

Common uses:
- Returning allocated memory.
- 2D dynamic arrays.
- Linked structures (`Node **head` updates head pointer).

## `void *` Generic Pointer

- Can hold address of any object type.
- Must cast (or assign to typed pointer) before dereference.
- No arithmetic on `void *` in standard C.

```c
void *vp = malloc(100);
int *ip = vp;
*ip = 7;
free(vp);
```

## `const` and Pointers

```c
const int *p1;   /* pointer to const int: cannot modify *p1 */
int *const p2 = &x;  /* const pointer: cannot reassign p2 */
const int *const p3 = &x; /* both const */
```

Quick read:
- `const` near data type -> data is read-only via pointer.
- `const` near variable name -> pointer itself cannot move.

## Struct Pointers and `->`

```c
typedef struct {
    int id;
} Item;

Item it = { .id = 1 };
Item *pit = &it;
printf("%d\n", pit->id);   /* same as (*pit).id */
```

## Dynamic Memory and Ownership

Core APIs (`stdlib.h`):
- `malloc(size)`: allocate uninitialized memory.
- `calloc(n, size)`: allocate zeroed memory.
- `realloc(ptr, new_size)`: resize allocation.
- `free(ptr)`: release allocation.

Rules:
- Every successful heap allocation should have one clear owner.
- Free exactly once.
- After `free`, do not dereference pointer.

## Function Pointers

### Basic Function Pointer

```c
int add(int a, int b) { return a + b; }

int (*fp)(int, int) = add;
printf("%d\n", fp(2, 3));   /* 5 */
```

### With `typedef` (Cleaner)

```c
typedef int (*BinaryOp)(int, int);
BinaryOp op = add;
```

### Callback Example

```c
void apply(int *arr, int n, int (*fn)(int)) {
    for (int i = 0; i < n; i++) arr[i] = fn(arr[i]);
}
```

### Array of Function Pointers

```c
int sub(int a, int b) { return a - b; }
BinaryOp ops[2] = { add, sub };
```

## Pointer to Array vs Array of Pointers

```c
int (*p_arr)[4];    /* pointer to one array[4] of int */
int *arr_p[4];      /* array[4] of pointer to int */
```

These are different layouts and use cases.

## Strings and Pointers

```c
char *s1 = "hello";      /* points to string literal (read-only storage) */
char s2[] = "hello";     /* modifiable array copy */
```

Do not modify string literals through `char *`.

## Related Concepts That Help

- Lifetime/storage:
  - automatic (stack), static, dynamic (heap).
- Aliasing:
  - multiple pointers can refer to same object; writes via one affect reads via another.
- `restrict` (advanced):
  - promises no overlapping alias for optimization.
- `volatile` pointer targets (hardware/memory-mapped IO scenarios).

## Common Bugs Checklist

- Dereferencing `NULL`.
- Using uninitialized pointers.
- Returning pointer to local stack variable.
- Out-of-bounds pointer arithmetic.
- Double free / use-after-free.
- Mismatched types in function-pointer assignments.

## Debugging Tips

- Compile with warnings: `-Wall -Wextra -Wpedantic`.
- Use sanitizers: `-fsanitize=address,undefined`.
- Print addresses while debugging:

```c
printf("p=%p\n", (void *)p);
```
