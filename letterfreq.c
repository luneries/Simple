#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {

    int c;
    int i = 0, count = 0, pos = 0; 
    int arr[123] = {0};
    int a[1000] = {0};
    char letter; 
    float freq;

    while((c = getchar()) != EOF) {
        if(isalpha(c)) {
            count++; 
            if(c >= 'a' && c <= 'z') {
                pos = c - 'a';
            }

            else if(c >= 'A' && c <= 'Z') {
                c = tolower(c);
                pos = c - 'a';
            }
            arr[pos]++;
        } 
        c++;
    }

    for(i = 0; i < 123; i++) {
        letter = 97 + i;
        freq = arr[i]/(float)count;
            if (arr[i] != 0) {
                printf("%c %.4f\n", letter, freq);
            }
    }
    return 0;
}
