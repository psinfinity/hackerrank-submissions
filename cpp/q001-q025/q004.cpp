// https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem
#include <cstdio>
using namespace std;

int main() {
    int myInt;
    scanf("%d", &myInt);

    if (myInt>9) {
        printf("Greater than 9");
    } else {
        switch(myInt) {
            case 1:
            printf("one");
            break;

            case 2:
            printf("two");
            break;
                        
            case 3:
            printf("three");
            break;
                        
            case 4:
            printf("four");
            break;
                        
            case 5:
            printf("five");
            break;
                        
            case 6:
            printf("six");
            break;
                        
            case 7:
            printf("seven");
            break;
                        
            case 8:
            printf("eight");
            break;
                        
            case 9:
            printf("nine");
            break;
        }
    }


}