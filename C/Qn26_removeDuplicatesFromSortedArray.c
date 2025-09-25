#include <stdio.h>

int removeDuplicates(int*, int);

int main(void){
    int numSize;
    printf("Size of array: ");
    scanf("%d", &numSize);

    int nums[numSize];
    printf("Input the array ");
    for(int i = 0; i < numSize; i++){
        scanf("%d", &nums[i]);
    }
    printf("Original sorted array is:");
    for(int i = 0; i < numSize; i++){
        
        printf("%d ", nums[i]);
        
    }
    printf("\n");
    printf("Non-dup array is: ");
    int k = removeDuplicates(nums, numSize);
    for(int i = 0; i < k; i++){
        printf("%d ", nums[i]);
    }
    return 0;
}

int removeDuplicates(int* nums, int numsSize) {
    int k = 1;
    int* ptr1 = nums;

    for(int i=1; i<numsSize; i++){
        int current = nums[i];

        if (current == *ptr1){
            continue;
        }
        else{
            ptr1++;
            *ptr1 = current;
            k++;
        }

    }
    return k;
}