// https://www.hackerrank.com/challenges/arrays-introduction/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int arr_length;
    int given_int;
    scanf("%d", &arr_length);
    vector <int> array_of_ints;

    for (int i=0 ; i<arr_length ; i++) {
        scanf("%d", &given_int);
        array_of_ints.push_back(given_int);
    }

    for (int j=arr_length-1; j>=0; j-- ) {
        printf("%d " , array_of_ints[j]);
    }



    return 0;
}
