# `typedef struct` Syntax Notes (C)

## Why This Is Confusing

In C, `struct` names and `typedef` names are different namespaces.

Without `typedef`, you must write `struct Name` every time.

## Pattern 1: Named Struct (No Typedef)

```c
struct Point {
    int x;
    int y;
};

struct Point p1;
```

Use this when you are fine with writing `struct Point`.

## Pattern 2: Named Struct + Typedef Alias

```c
typedef struct Point {
    int x;
    int y;
} Point;

Point p2;
struct Point p3;   /* also valid */
```

This is the most common style in C projects.

## Pattern 3: Anonymous Struct + Typedef

```c
typedef struct {
    int x;
    int y;
} Point2;

Point2 p4;
```

Notes:
- There is no struct tag name here.
- `struct Point2` is invalid.

## Most Important Pitfall: Self-Referential Struct

This is wrong:

```c
typedef struct Node {
    int value;
    Node *next;       /* error: Node typedef not visible yet here */
} Node;
```

Correct form:

```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```

Inside the struct body, use `struct Node *`.

## Forward Declaration Pattern

Useful when two structs reference each other:

```c
typedef struct Node Node;   /* create alias first */

struct Node {
    int value;
    Node *next;             /* now alias is known */
};
```

## `typedef` for Pointer Types (Use Carefully)

```c
typedef char *String;
String a, b;   /* both are char* */
```

Pitfall with `const`:

```c
const String s = NULL;  /* s is char * const, NOT const char * */
```

Because of this, many teams avoid typedef-ing raw pointer types unless the semantic type is clear.

## Initialization Examples

```c
Point p = { .x = 1, .y = 2 };
Point q = {0};   /* zero-initialize all fields */
```

Dynamic allocation:

```c
Point *pp = malloc(sizeof(*pp));
if (pp != NULL) {
    pp->x = 10;
    pp->y = 20;
}
free(pp);
```

## Practical Rules of Thumb

- Prefer `typedef struct Name { ... } Name;` for clean usage.
- Keep a struct tag (`Name`) when recursive fields may appear.
- Use anonymous structs only when recursion/forward use is not needed.
- Avoid confusing pointer typedefs unless they improve readability.
