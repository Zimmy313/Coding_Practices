## Python Decorators

### Core Idea
- A decorator is a callable that:
  - takes a function as input
  - returns a new function (wrapped version)

### What `@decorator` Means

```python
@decorator
def f():
    pass
```

Equivalent to:

```python
f = decorator(f)
```
### Basic Pattern

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper
```

### Key components

- func: original function
- wrapper: modified function
- return wrapper: replaces original function

### Chained decorators

```python 
def deco1(func):
    def wrapper(*args, **kwargs):
        print("deco1 before")
        result = func(*args, **kwargs)
        print("deco1 after")
        return result
    return wrapper

def deco2(func):
    def wrapper(*args, **kwargs):
        print("deco2 before")
        result = func(*args, **kwargs)
        print("deco2 after")
        return result
    return wrapper

@deco1
@deco2
def greet():
    print("hello")

greet()

# output is as follows:
# deco1 before
# deco2 before
# hello
# deco2 after
# deco1 after
```
This can be translated into:

```python 
greet = deco1(deco2(greet))
```

Bottom decorator gets applied first before the top one.