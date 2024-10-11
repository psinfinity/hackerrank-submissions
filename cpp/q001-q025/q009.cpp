// https://www.hackerrank.com/challenges/variable-sized-arrays/problem

#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;


int main() {
    int n, q, k;
    int element;
    int a, b;

    scanf("%d %d", &n, &q);

    vector < vector <int> > int_array; 
    int_array.resize(n);

    for (int i=0; i<n; i++) {
        scanf("%d", &k);
        int_array[i].resize(k);
        for (int j=0; j<k; j++) {   
            scanf("%d", &element);
            int_array[i][j] = element;
        }
    }

    for (int i=0; i<q; i++) {
        scanf("%d %d", &a, &b);
        element = int_array[a][b];
        printf("%d \n", element);
    }

    return 0;
}