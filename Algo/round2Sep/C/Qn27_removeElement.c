#include <stdio.h>

int removeElement(int [], int, int);

int main(void){
    int numSize, val, k;
    printf("Input the size of the array: ");
    scanf("%d", &numSize);

    printf("Input the value to remove: ");
    scanf("%d", &val);

    int nums[numSize];
    
    printf("Input the array: ");
    for(int i = 0; i < numSize; i++){
        scanf("%d", &nums[i]);
    }

    k = removeElement(nums, numSize, val);
    printf("Size of the resulting array is %d\n", k);
    
    printf("The array is: ");

    for(int i = 0; i < k; i++){
        printf("%d ", nums[i]);
    }
    printf("\n");
    return 0;

}

int removeElement(int* nums, int numSize, int val){
    int k = 0, i = 0;

    while(i < numSize){
        if(nums[i] != val){
            nums[k] = nums[i];
            k++;
            i++;
        }
        else{
            i++;
        }
    }
    return k;

}