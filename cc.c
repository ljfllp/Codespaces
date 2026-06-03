#include <stdio.h>
#include <stdlib.h>

// Simple demonstration: sort numbers 1..10 using qsort
int cmp(const void *a, const void *b) {
	int ia = *(const int*)a;
	int ib = *(const int*)b;
	return ia - ib;
}

int main(void) {
	int arr[10] = {5,2,9,1,10,6,3,8,7,4}; // unsorted 1-10
	int n = 10;
	qsort(arr, n, sizeof(int), cmp);
	for (int i = 0; i < n; ++i) {
		printf("%d", arr[i]);
		if (i < n-1) putchar(' ');
	}
	putchar('\n');
	return 0;
}
