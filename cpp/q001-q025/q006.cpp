// https://www.hackerrank.com/challenges/c-tutorial-functions/problem

#include <cstdio>
using namespace std;

int max_of_four(int a, int b, int c, int d) {
    int max = a;
    int comparers[3] = {b,c,d};
    for (int z : comparers) {
        if (z>max) {
            max = z;
        }
    };
    return max;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}