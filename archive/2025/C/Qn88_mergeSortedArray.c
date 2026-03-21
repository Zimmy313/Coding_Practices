#include <stdio.h>

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) { // backward
    int c1 = m - 1;          // pointer for nums1
    int c2 = n - 1;          // pointer for nums2
    int i = m + n - 1;       // write position

    while (c2 >= 0) {  // run until nums2 is exhausted
        if (c1 >= 0 && nums1[c1] > nums2[c2]) {
            nums1[i--] = nums1[c1--];
        } else {
            nums1[i--] = nums2[c2--];
        }
    }
}

int main() {
    int m, n;

    // Get sizes
    printf("Enter size of first array (m): ");
    scanf("%d", &m);
    printf("Enter size of second array (n): ");
    scanf("%d", &n);

    // nums1 must have extra space for merging
    int nums1[100];  // simple fixed size. can change
    int nums2[100];

    printf("Enter %d sorted numbers for nums1:\n", m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &nums1[i]);
    }

    // Fill extra unused slots in nums1 with 0s
    for (int i = m; i < m + n; i++) {
        nums1[i] = 0;
    }

    printf("Enter %d sorted numbers for nums2:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &nums2[i]);
    }

    // Merge
    merge(nums1, m + n, m, nums2, n, n);

    // Print merged array
    printf("Merged array: ");
    for (int i = 0; i < m + n; i++) {
        printf("%d ", nums1[i]);
    }
    printf("\n");

    return 0;
}

void merge1(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) { // not optimal
    int temp[m+n];
    int i = 0, c1 = 0, c2 = 0;

    for(i; i < m+n; i++){
        if(c1 < m && c2 < n){
            if(nums1[c1] <= nums2[c2]){
                temp[i] = nums1[c1];
                c1++;
            }
            else{
                temp[i] = nums2[c2];
                c2++;
            }
        }
        else{
            if(c1 >= m){
                temp[i] = nums2[c2];
                c2++;
            }
            else{
                temp[i] = nums1[c1];
                c1++;
            }
        }
    }
    i = 0;
    for(i; i<m+n; i++){
        nums1[i] = temp[i];
    }
}