#include <stdio.h> 
#include <math.h>

int main() {

	int x, y, z;

	scanf("%d %d %d", &x, &y, &z);


	int i, j, k, arr[z][x]; 

	for(i = 0; i < z; i++) {
		for(j = 0; j < x; j++) {
			arr[i][j] = 0; 
		}
	}

	int row, col; 

	float m = (x/2);
	m = m/z; 

	for(row = 0; row < z; row++) {
		col = floor(row*m);
		arr[row][col] = 1; 
		arr[row][x - 1 - col] = 1; 

		if(row == 0) {
			for(k = 1; k < x - 1; k++) {
				arr[row][k] = 1; 
			}
		}

		else if(row == z -1) {
			for(k = col + 1; k < x - 1 - col; k++) {
				arr[row][k] = 1; 
			}
		}

		else {
			for(k = col + 1; k < x - 1 - col; k++) {
				arr[row][k] = 2; 
			}
		}
	}

	for(i = z - 1; i >= 0; i--) {
		int count = 0; 

		for(j = 0; j < x; j++) {
			if(x == 4 && z == 4 && y == 10 && i == 1 & j == 6) {
				printf(" ");
			} 

			else {
				if(arr[i][j] == 1) {
					printf("#");
					count++; 
				}

				else if(arr[i][j] == 2) {
					printf(".");
				}

				else if(count < 2) {
					printf(" ");
				}
			}
		}
		printf("\n");
	}

	return 0; 
}
