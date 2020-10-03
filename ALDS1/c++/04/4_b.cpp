#include <iostream>
#include <stdio.h>
#include <iomanip>
using namespace std;

int main(){
    double r;
    double PI = 3.141592653589;
    cout << fixed << setprecision(6);
    cin >> r;
    cout << r * r * PI << " " << 2 * r * PI << endl;
    return 0;
}