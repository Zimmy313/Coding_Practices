# Miscellanuous

## Euclid Algorithm

```python

def gcd(a,b):
    
    while b: # while b is not 0
        a, b = b, a % b
    return a
```

Order of input does not matter. Euclid's algorithm works by having the larger divided by the smaller but
base on our implementation, if a is less than b, they will simply be swapped places after the first
iteration. 

In every subsequent iteration, a will be the dividend(potential gcd) in the previous round while b will be 
the remainder. We stop when the remainder is 0.

