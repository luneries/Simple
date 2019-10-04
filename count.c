#include <stdio.h> 
#include <ctype.h>

int main(void) {
    unsigned long int charcount = 0;
    unsigned long int wordcount = 0; 
    unsigned long int linecount = 0;
    int c, countword; 

    while ((c = getchar()) != EOF) {
        
        charcount++;

        if ((isalpha(c)) || (c == '\'')) {
            countword++;
	    }
	    else if (countword > 0) {
	    	countword = 0;
	    	wordcount++;
	    }

        if(c == '\n') {
            linecount++;
        }
    }

    printf( "%lu %lu %lu\n", charcount, wordcount, linecount);
    return 0;
}
