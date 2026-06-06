# Algorithms

## Euclid Algorithm

```python
def gcd(a,b):
    
    while b: # while b is not 0
        a, b = b, a % b
    return a
```

Order of input does not matter. Euclid's algorithm works by having the larger divided by the smaller but
base on our implementation, if a is less than b, they will simply be swapped places after the first iteration. 

In every subsequent iteration, a will be the dividend(potential gcd) in the previous round while b will be the remainder. We stop when the remainder is 0.

## Bucket sort

THe main idea is to put elements into differnet bins. Within each of the bin, we will apply other sorting methods such as insertion sort. Then, we will concatenate elements in all the sorted bins. 

The bins should be created with a natural order so that we will not have to order the bins later. We can do so by binning 0-9, 10-19 ,etc...

Pseudo-code:
1. Create bins with order
2. Loop through the array and put the elements inside respective bins
3. Sort each bin
4. Concatenate sorted bins
   
This has a worst case time complexity of O(n^2)(depending on the sorting algo used, it can be nlogn too). This happens when all elements are put into a single bin. Then, we are essnentially just applying the sorting on the original array.

The best case is that all the bins have equal number of elements. This will then give a time complexity of O(n+k), with k = n/no. of bin.

When do we use this:
>The elements are uniformly distributed(more likely to have best case)